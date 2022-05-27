#!/usr/bin/env python3

#TODO optimize imports
import os, sys, argparse
from time import perf_counter
from subprocess import check_call, STDOUT, Popen, PIPE, check_output
from tempfile import NamedTemporaryFile
import re, json




from prettytable import PrettyTable
import plotext
from colorama import Fore, Style
import matplotlib.pyplot as plt


with open("./src/rounds.txt", "r") as f:
    ROUNDS = int(f.read())



SLOW_LANGUAGES = {
    "Python": "python3 main.py",
    "C++": "g++ main.cpp -o main && ./main",
    "JavaScript": "node main.js",
    "TypeScript": "deno run --allow-read --allow-hrtime main.ts",
    "Java": "javac main.java && java -cp ./ main",
    "C#": "dotnet run",
    "Lua": "lua main.lua",
    "Php": "php main.php",
    "Ruby": "ruby main.rb",
    "Go": "go run main.go",
    "Rust": "rustc main.rs && ./main",
    "Powershell": "pwsh main.ps1",
    "Swift": "swift main.swift",
    "Dart": "dart run main.dart",
}


FAST_LANGUAGES = {
    "Python": "pypy3 main.py",
    "C++": "g++ -O3 -o main main.cpp && ./main",
    "JavaScript": "node main.js",
    "TypeScript": "deno run --allow-read --allow-hrtime main.ts",
    "Java": "javac main.java && java -cp ./ main",
    "C#": "dotnet run -c Release",
    "Lua": "lua main.lua",
    "Php": "php main.php",
    "Ruby": "ruby main.rb",
    "Go": "go build -o main main.go && ./main",
    "Rust": "cargo build --release && ./target/release/main",
    "Powershell": "pwsh main.ps1",
    "Swift": "swiftc main.swift -Ounchecked && ./main",
    "Dart": "dart compile exe main.dart --verbosity warning -o main && ./main",
}



SLOW_CHANGED_LANGUAGES = SLOW_LANGUAGES.copy()
FAST_CHANGED_LANGUAGES = FAST_LANGUAGES.copy()


SLOW_LANGUAGES_RESULTS = {}
FAST_LANGUAGES_RESULTS = {}


def cleanup() -> None:
    pass


def change_round() -> None:
    with open("./src/rounds.txt", "w") as f:
        f.write(str(ROUNDS))


#possibly remove most of this cauz it's kinda not needed
def name_to_abbr(reverse: bool = True, entry_languages: dict[str, str] | list[str] = SLOW_CHANGED_LANGUAGES, capitalize: bool = False, single: bool = False, single_name: str = None) -> dict[str, str] | list[str]:
    """Helper function to convert language names to their abbreviation or vice-versa.

    Args:
        reverse (bool, optional): If wanted reverse. Defaults to True.
        entry_languages (dict[str, str] | list[str], optional): The list or dict of the languages. Defaults to SLOW_CHANGED_LANGUAGES.
        capitalize (bool, optional): If you want to capitalize. Defaults to False.
        single (bool, optional): Only return the name. Defaults to False.
        single_name (str, optional): The single name. Defaults to "".

    Returns:
        dict[str, str] | list[str]: Return dict if dict was given, else list.
    """



    if single:
        match single_name:
            case "Csharp" | "Cs":
                return "C#"
            case "Cpp":
                return "C++"
            case "Js" | "Node":
                return "JavaScript"
            case "Ts" | "Deno":
                return "TypeScript"
            case "Py" | "Pypy":
                return "Python"
            case "Go":
                return "Golang"
            case "Pwsh":
                return "Powershell"
            case _:
                return single_name



    if not entry_languages:
        entry_languages = SLOW_LANGUAGES.copy()
    languages_type = type(entry_languages)
    #checking if dict and if so convert to list
    if languages_type == dict:
        languages_values = entry_languages.values()
        entry_languages = entry_languages.keys()


    new_languages = []
    #abbreviation to normal
    if reverse:
        for language in entry_languages:
            match language.lower():
                case "c#":
                    new_languages.append("csharp")
                case "c++":
                    new_languages.append("cpp")
                case "py":
                    new_languages.append("python")
                case "go":
                    new_languages.append("golang")
                case "pwsh":
                    new_languages.append("powershell")
                case _:
                    new_languages.append(language.lower())



    #normal to abbreviation
    else:
        for language in entry_languages:
            match language.lower():
                case "csharp" | "cs":
                    new_languages.append("c#")
                case "cpp":
                    new_languages.append("c++")
                case "py":
                    new_languages.append("python")
                case "golang":
                    new_languages.append("go")
                case "powershell":
                    new_languages.append("pwsh")
                case _:
                    new_languages.append(language.lower())


    if capitalize:
        new_languages = [language.capitalize() for language in new_languages]




    if languages_type == dict:
        return_languages = {}
        #for value in languages_values:
            #for language in new_languages:
                #return_languages[language] = value
                #print(return_languages)
        #return return_languages
        for language, value in zip(new_languages, languages_values):
            return_languages[language] = value
        return return_languages


    return new_languages












#TODO maybe put the check_call in a subfunction
def call_languages(MODE: str, PROCESS_MODE: str) -> dict[str: float]:
    """Function that calls the languages and captures the output(version and execution time) and gets the compile time with the GNU Time command.

    Returns:
        dict[str: float]: Return total time taken by languages.
    """
    DOCKER = os.environ.get("DOCKER", False)

    def special_cases(output: list, language: str, mode: str) -> list:
        """Helper function that handles languages that print more info than it's needed.

        Args:
            output (list): The output of the language.

        Returns:
            list: The filtered output of given language.
        """
        
        #insert the swift version cauz swift is hard on linux
        if language == "swift":
            output.insert(0, check_output(["swift", "--version"]).decode("utf-8").split()[2])

        elif language == "rust" and mode == "fast":
            output = output[6:]
        elif language == "lua":
            del output[0]
            
        elif language == "dart" and mode == "fast":
            output = output[2:]

        elif DOCKER:
            if language == "typescript":
                output = output[2:]

        return output




    def sync_call(languages: dict[str, str], mode: str) -> None:
        """Helper function to call the languages sequentially.

        Args:
            languages (dict[str, str]): The dict of languages to be benchmarked.
            mode (str): The mode either slow or fast.
        """
        for language, command in languages.items():
            print(f"\rCurrently on -> {Style.BRIGHT + Fore.RED}{language.capitalize()}{Style.RESET_ALL}.        ", end="\r")
            path = os.path.join("./src/", language, mode)
            with NamedTemporaryFile() as f:
                ##TODO remove shell=True and the extra sh
                check_call(f'/usr/bin/time -f " %e %P %M" sh -c  "{command}" ', shell=True, stdout=f, stderr=STDOUT, cwd=path)
                f.seek(0)
                output = f.read().decode("utf-8").split()
            #remove the cargo confirmation



            output = special_cases(output, language, mode)




            total_time = float(output[2])
            output[2] = float(output[2]) - float(output[1])
            output.append(total_time)
            #set the results into the corresponding dict
            exec(f"{mode.upper()}_LANGUAGES_RESULTS[language] = output")



    def async_call(languages: dict[str, str], mode: str) -> None:
        """Helper function that calls the languages in parallel.

        Args:
            languages (dict[str, str]): The dict of languages to be benchmarked.
            mode (str): The mode either slow or fast.
        """
        processes = []
        for language, command in languages.items():
            print(f"\rCurrently on -> {Style.BRIGHT + Fore.RED}{language.capitalize()}{Style.RESET_ALL}.        ", end="\r")
            path = os.path.join("./src/", language, mode)
            #named open temp file
            f = NamedTemporaryFile()
            process = Popen(f'/usr/bin/time -f " %e %P %M" sh -c  "{command}" ', shell=True, cwd=path, stdout=f, stderr=STDOUT)
            processes.append((process, f))
        #wait for all processes to finish and get the output
        for index, (process, f) in enumerate(processes):
            out, error = process.communicate()
            f.seek(0)
            output = f.read().decode("utf-8").split()
            f.close()
            #output = output.decode("utf-8").split()
            if error: print(Fore.RED + error + Fore.RESET); break
            language = list(languages.keys())[index]


            output = special_cases(output, language, mode)



            total_time = float(output[2])
            output[2] = float(output[2]) - float(output[1])
            output.append(total_time)
            #set the results into the corresponding dict
            exec(f"{mode.upper()}_LANGUAGES_RESULTS[language] = output")

    return_times = {}
    #normal
    if MODE in ["slow", "both"]:
        languages = name_to_abbr()
        start = perf_counter()
        if PROCESS_MODE == "sync":
            sync_call(languages, "slow")
        else:
            async_call(languages, "slow")

        end = perf_counter() - start
        return_times["slow"] = end


    if MODE in ["fast", "both"]:
        languages = name_to_abbr(entry_languages=FAST_CHANGED_LANGUAGES)
        start = perf_counter()
        if PROCESS_MODE == "sync":
            sync_call(languages, "fast")
        else:
            async_call(languages, "fast")

        end = perf_counter() - start
        return_times["fast"] = end

    return return_times








def clear() -> None:
    """Helper function to clear the terminal.
    """
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def arg_parser() -> argparse.Namespace:
    #TODO add the ability to change the mode
    parser = argparse.ArgumentParser(description="Calculate the prime numbers between any given range.")
    parser.add_argument("-c", "--custom", help="Enter a custom rounds value.", type=int)
    parser.add_argument("-n", "--nogui", help="Use this if you don't want to use graphical graphs.", action="store_true")
    args = parser.parse_args()
    return args

def save_results(table: PrettyTable) -> None:
    """Function that saves the results into multiple formats.

    Args:
        table (PrettyTable): The table to be saved.
    """


    #regex to filter out all the ansi escape sequences
    ansi_regex = r'\x1b(' \
                r'(\[\??\d+[hl])|' \
                r'([=<>a-kzNM78])|' \
                r'([\(\)][a-b0-2])|' \
                r'(\[\d{0,2}[ma-dgkjqi])|' \
                r'(\[\d+;\d+[hfy]?)|' \
                r'(\[;?[hf])|' \
                r'(#[3-68])|' \
                r'([01356]n)|' \
                r'(O[mlnp-z]?)|' \
                r'(/Z)|' \
                r'(\d+)|' \
                r'(\[\?\d;\d0c)|' \
                r'(\d;\dR))'
    ansi_escape = re.compile(ansi_regex, flags=re.IGNORECASE)

    #SAVE to csv  
    csv_string = ansi_escape.sub("", table.get_csv_string())
    with open("./results/results.csv", "a") as outcsv:
        outcsv.write(csv_string + "\n")



        
    results_json = []
    results_json.append(SLOW_LANGUAGES_RESULTS)
    results_json.append(FAST_LANGUAGES_RESULTS)
    with open("./results/results.json", "w") as outjson:
        json.dump(results_json, outjson, indent=4)




def table_and_graph(total_time: float, nogui: bool, MODE: str, times: list[float]) -> None:
    """Function that creates the tables and graphs.

    Args:
        total_time (float): The total time of each language.
        nogui (bool): If the user wants gui or not.
        MODE (str): The mode either slow or fast.
        times (list[float]): The total time.
    """
    total_cpu_time = []

    def graph(languages_array: list, mode: str) -> None:
        """Helper function that creates the graphs.

        Args:
            languages_array (list): The languages array.
            mode (str): The mode either slow or fast.
        """
        x = name_to_abbr(False, list(languages_array.keys()), True)
        y = []
        xlabels = "Languages"
        ylabels = ["Times (s)", "Time (s)", "Time (s)", "Memory (kB)"]
        titles = ["Total time per language", "Execution time per language", "Compilation/Interpretation time per language", "Peak memory usage per language"]




        total_time_language = list(map(lambda x: round(x[:][-1], 4), list(languages_array.values())))
        y.append(total_time_language)   

        execution_time_language = list(map(lambda x: round(float(x[:][1]), 4), list(languages_array.values()))) 
        y.append(execution_time_language)   

        compilation_time_language = list(map(lambda x: round(float(x[:][2]), 4), list(languages_array.values())))
        y.append(compilation_time_language)   

        memory_language = list(map(lambda x: int(x[:][4]), list(languages_array.values())))
        y.append(memory_language)   
        


        if not nogui:
            for index, _y in enumerate(y):
                ylabel = ylabels[index]
                title = titles[index]
                i = index; i += 1
                
                plt.subplot(2, 2, i)
                plt.bar(x, _y)
                plt.xlabel(xlabels)
                plt.ylabel(ylabel)
                plt.title(title)
                plt.savefig(fname=f"./results/graphs_{mode}.png")
                plt.grid()
        else:
            plotext.subplots(2, 2)
            for index, _y in enumerate(y):
                ylabel = ylabels[index]
                title = titles[index]
                i = index; i += 1
                match i:
                    case 1:
                        plotext.subplot(1, 1)
                    case 2:
                        plotext.subplot(1, 2)
                    case 3:
                        plotext.subplot(2, 1)
                    case 4:
                        plotext.subplot(2, 2)

                plotext.bar(x, _y)
                plotext.xlabel(xlabels)
                plotext.ylabel(ylabel)
                plotext.title(title)
                plotext.grid()
            plotext.savefig(f"./results/graphs_{mode}.png")


    def table(results_list: list, total_times: float) -> None:
        """Helper function that creates the tables.

        Args:
            results_list (list): The results list.
            total_times (float): The total times for each language.
        """
        #TODO CENTER TABLE
        #terminal_with = os.get_terminal_size().columns
        
        my_table = PrettyTable(
            [
                Fore.RED + "Language" + Fore.RESET,
                Fore.GREEN + "Total time (s)" + Fore.RESET,
                Fore.BLUE + "Execution time (s)" + Fore.RESET,
                Fore.CYAN + "Compilation / Interpretation time (s)" + Fore.RESET,
                Fore.LIGHTGREEN_EX + "Peak Memory usage (kB)" + Fore.RESET,
                Fore.MAGENTA + "Version" + Fore.RESET,
            ]
        )


        total_execution_time = 0
        total_compilation_time = 0
        total_memory_usage = 0

        for language, output in name_to_abbr(False, results_list, True).items():
            for result in output:
                if result is output[1]:
                    total_execution_time += float(result)
                elif result is output[2]:
                    total_compilation_time += float(result)
                elif result is output[4]:
                    total_memory_usage += int(result)
            
            my_table.add_row([
                language,
                round(float(output[-1]), 4),#total time
                round(float(output[1]), 4), #execution time
                round(float(output[2]), 4), #compilation time
                output[4], #memory usage
                output[0]  #version
            ])
        
        total_total_time = total_execution_time + total_compilation_time
        total_cpu_time.append(total_total_time)

        my_table.add_row([
            Fore.RED + f"Total ({len(results_list)})" + Fore.RESET, #total languages
            Fore.GREEN + str(round(total_total_time, 4)) + Fore.RESET, #sum of all total times 
            Fore.BLUE + str(round(total_execution_time, 4)) + Fore.RESET, #sum of all execution times
            Fore.CYAN + str(round(total_compilation_time, 4)) + Fore.RESET, #sum of all compilation times
            Fore.LIGHTGREEN_EX + str(total_memory_usage) + Fore.RESET, #sum of all peak memory usages
            Fore.MAGENTA + "####" + Fore.RESET ####
        ])

        save_results(my_table)
        #print(my_tablet_csv_string())
        print(my_table)

    if MODE in ["slow", "both"]:
        print("\n")
        print(f"{Fore.LIGHTGREEN_EX}Slow mode{Fore.RESET}".center(128))
        table(SLOW_LANGUAGES_RESULTS, times["slow"])
        #graphs

        graph(SLOW_LANGUAGES_RESULTS, "slow")
        if not nogui:
            plt.suptitle("Graphs")
            plt.get_current_fig_manager().set_window_title("Results")
            plt.show()
        else:
            plotext.show()

        #save graphs
        #plt.savefig(fname="./results/graphs.png")

    if MODE in ["fast", "both"]:
        print(f"{Fore.LIGHTGREEN_EX}Fast mode{Fore.RESET}".center(128))
        table(FAST_LANGUAGES_RESULTS, times["fast"])

        graph(FAST_LANGUAGES_RESULTS, "fast")
        if not nogui:
            plt.suptitle("Graphs")
            plt.get_current_fig_manager().set_window_title("Results")
            plt.show()
        else:
            plotext.show()

        #save graphs
        #plt.savefig(fname="./results/graphs.png")
    print("\nIn total this all comparison took: " + Fore.GREEN + str(round(total_time, 3)) + Fore.RESET + f" seconds in {Style.BRIGHT}REAL time{Style.RESET_ALL} and in {Style.BRIGHT}CPU time{Style.RESET_ALL} it took: {Fore.GREEN}{round(sum(total_cpu_time), 4)}{Fore.RESET} seconds.")
    print(f"\nResults saved in {Fore.YELLOW}./results/*" + Fore.RESET)

#TODO maybe add a while loop for wrong inputs
def menu(nogui: bool) -> None:
    """This function creates the main menu.

    Args:
        nogui (bool): If the user wants gui or not.

    Raises:
        KeyboardInterrupt: Bye bye.
    """
    global ROUNDS 
    MODE = "both"
    PROCESS_MODE = "sync"
    clear()
    start_input = ""
    while (start := start_input.lower()) not in ["start", "play"] :
        if start in ["exit", "quit", "leave"]:
            raise KeyboardInterrupt
        elif start in ["options", "config", "settings"]:
            clear()
            print(f"{Fore.MAGENTA + 'Choose one of the following options to change' + Fore.RESET}:    {Fore.CYAN + '(R)ounds' + Fore.RESET}    {Fore.LIGHTBLUE_EX + '(L)anguages' + Fore.RESET}    {Fore.MAGENTA + '(P)Rocess' + Fore.RESET}    {Fore.LIGHTYELLOW_EX + '(M)ode' + Fore.RESET}    {Fore.LIGHTGREEN_EX + '(G)raphs' + Fore.RESET}    {Fore.RED + '(B)ack' + Fore.RESET}")
            options_input = input(f"{Fore.BLUE}options{Fore.RESET}> ")
            options_input = options_input.lower()
            #rounds
            if options_input in ["rounds", "round", "r"]:
                
                clear()
                print("The current Rounds are set to: " + Fore.LIGHTCYAN_EX + str(ROUNDS) + Fore.RESET)
                print("Type the rounds you want to change to!")
                rounds_input = input(f"{Fore.BLUE}options{Fore.RESET}/{Fore.CYAN}rounds{Fore.RESET}> ")
                if rounds_input.isdigit():
                    ROUNDS = int(rounds_input)
                    if ROUNDS > 10000:
                        print(Fore.YELLOW + "WARNING: The rounds are set to a high value, this might take a while!" + Fore.RESET)
                    print(f"{Fore.GREEN}Rounds set to {ROUNDS}." + Fore.RESET)
                else:
                    print(f"{Fore.LIGHTRED_EX}Invalid rounds value." + Fore.RESET) 
            

            elif options_input in ["process", "p", "processess"]:
                clear()
                print("The current Processess mode are set to: " + Fore.LIGHTCYAN_EX + PROCESS_MODE.capitalize() + Fore.RESET + ".")
                print(f"Type the processess mode you want to change to!\nEnter either {Fore.LIGHTGREEN_EX}'sync/sequence'{Fore.RESET} or {Fore.LIGHTGREEN_EX}'async/parallel'{Fore.RESET}.")
                process_input = input(f"{Fore.BLUE}options{Fore.RESET}/{Fore.MAGENTA}process{Fore.RESET}> ")
                if process_input in ["sync", "sequence"]:
                    PROCESS_MODE = "sync"
                    print(f"{Fore.GREEN}Processess mode set to {PROCESS_MODE}." + Fore.RESET)
                elif process_input in ["async", "parallel"]:
                    PROCESS_MODE = "async"
                    print(f"{Fore.GREEN}Processess mode set to {PROCESS_MODE}." + Fore.RESET)
                else:
                    print(f"{Fore.LIGHTRED_EX}Invalid processess mode." + Fore.RESET)



            elif options_input in ["mode", "m"]:
                clear()
                print("The current Mode is set to: " + Fore.LIGHTMAGENTA_EX + MODE.capitalize() + Fore.RESET)
                print("Type the mode you want to change to (both, optimized or unoptimized)!")
                mode_input = input(f"{Fore.BLUE}options{Fore.RESET}/{Fore.LIGHTYELLOW_EX}mode{Fore.RESET}> ")
                if mode_input.lower() in ["fast", "optimized"]:
                    MODE = "fast" 
                    print(f"{Fore.GREEN}Mode set to {MODE}." + Fore.RESET)
                elif mode_input.lower() in ["slow", "unoptimized"]:
                    MODE = "slow"
                    print(f"{Fore.GREEN}Mode set to {MODE}." + Fore.RESET)
                elif mode_input.lower() == "both":
                    MODE = "both"
                    print(f"{Fore.GREEN}Mode set to {MODE}." + Fore.RESET)

                else:
                    print(f"{Fore.LIGHTRED_EX}Invalid mode value." + Fore.RESET)


            elif options_input in ["language", "languages", "l"]:
                clear()
                #if no changed languages show all
                if SLOW_CHANGED_LANGUAGES == SLOW_LANGUAGES:
                    print("The current Languages are set to: " + Fore.LIGHTCYAN_EX + ", ".join(map(str, SLOW_LANGUAGES.keys())) + Fore.RESET)
                
                else: #if changed languages show changed and available
                    print("The current Languages are set to: " + Fore.LIGHTCYAN_EX + ", ".join(map(str, SLOW_CHANGED_LANGUAGES)) + Fore.RESET)
                    print("The available Languages are set to: " + Fore.LIGHTMAGENTA_EX + ", ".join(map(str, SLOW_LANGUAGES.keys())) + Fore.RESET)

                print(f"Type the languages you want to change to! Split them with a comma, and prefix the language with {Fore.MAGENTA}'?'{Fore.RESET} to remove it.")
                languages_input = input(f"{Fore.BLUE}options{Fore.RESET}/{Fore.LIGHTBLUE_EX}languages{Fore.RESET}> ").replace(" " , "").split(",")
                for language_input in languages_input:
                    try:




                        if (capitalized_language := name_to_abbr(single=True, single_name=language_input.lower().capitalize())) in SLOW_LANGUAGES.keys():
                            #SLOW_CHANGED_LANGUAGES.clear()
                            SLOW_CHANGED_LANGUAGES[capitalized_language] = SLOW_LANGUAGES[capitalized_language]
                            FAST_CHANGED_LANGUAGES[capitalized_language] = FAST_LANGUAGES[capitalized_language]

                            print(f"{Fore.GREEN}Language {capitalized_language} added." + Fore.RESET)

                        elif language_input[0] == "?":
                            language_name = language_input[1:].lower().capitalize()
                            language_name = name_to_abbr(single=True, single_name=language_name)
                            if language_name in SLOW_CHANGED_LANGUAGES.keys():
                                SLOW_CHANGED_LANGUAGES.pop(language_name)
                                FAST_CHANGED_LANGUAGES.pop(language_name)

                                print(f"{Fore.MAGENTA}Language {language_name} removed." + Fore.RESET)
                            else:
                                print(f"{Fore.LIGHTRED_EX}Language {language_name} not found." + Fore.RESET) 

                        else:
                            print(f"{Fore.LIGHTRED_EX}Language {language_input} not found." + Fore.RESET)

                    except IndexError:
                        print(Fore.LIGHTRED_EX + "Invalid language." + Fore.RESET) 


            elif options_input in ["graph", "graphs", "g"]:
                GRAPH_MODE = "GUI" if nogui == False else "Terminal"
                print("Currently the graph mode is set to: " + Fore.LIGHTMAGENTA_EX + GRAPH_MODE + Fore.RESET)
                print("Type the graph mode you want to change to (GUI or Terminal)!")
                graph_input = input(f"{Fore.BLUE}options{Fore.RESET}/{Fore.GREEN}graphs{Fore.RESET}> ")
                if graph_input.lower() in ["gui", "graphical", "graph"]:
                    nogui = False
                    print(f"{Fore.GREEN}Graph mode set to {graph_input.capitalize()}." + Fore.RESET)
                elif graph_input.lower() in ["terminal", "nogui", "tui"]:
                    nogui = True
                    print(f"{Fore.GREEN}Graph mode set to {graph_input.capitalize()}." + Fore.RESET)
                else:
                    print(f"{Fore.LIGHTRED_EX}Invalid graph mode." + Fore.RESET)
                


        elif start in ["info", "information", "details"]:
            print(f"The comparison will run in {Style.BRIGHT + PROCESS_MODE.capitalize() + Style.RESET_ALL} mode with {Fore.RED + str(ROUNDS) + Fore.RESET} iterations and the following {Style.BRIGHT + str(len(SLOW_CHANGED_LANGUAGES)) + Style.RESET_ALL} languages: {Fore.MAGENTA + ', '.join(map(str, SLOW_CHANGED_LANGUAGES)) + Fore.RESET}\nIf your having difficulties check Known Bugs in README.md.")



        start_input = input(
            f"Enter either {Fore.RED}'start'{Fore.RESET} to start the speed comparison, {Fore.BLUE}'options'{Fore.RESET} to change the default config, {Fore.GREEN}'info'{Fore.RESET} for the current program information or {Fore.MAGENTA}'quit'{Fore.RESET} to exit.\n->"
        )


        #if none of the above
        clear()
    change_round()
    print(f"This comparison will run up to {Fore.RED + str(ROUNDS) + Fore.RESET} iterations in {Style.BRIGHT + PROCESS_MODE.capitalize() + Style.RESET_ALL} mode and it is using {Style.BRIGHT + str(len(SLOW_CHANGED_LANGUAGES.keys())) + Style.RESET_ALL} languages: {Fore.MAGENTA + ', '.join(map(str, SLOW_CHANGED_LANGUAGES.keys())) + Fore.RESET}")


    #start actual benchmark
    start_benchmark = perf_counter()
    times = call_languages(MODE, PROCESS_MODE)
    total_benchmark = perf_counter() - start_benchmark
    print(Fore.LIGHTGREEN_EX + "Done!                                                                        " + Fore.RESET)
    table_and_graph(total_benchmark, nogui, MODE, times)





def main() -> None:
    """Main function of the program that calls all others.
    """
    global ROUNDS
    args = arg_parser()
    if args.custom:
        ROUNDS = args.custom
    if args.nogui:
        nogui = True 
    else:
        nogui = False

    menu(nogui)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nBye..." + Fore.RESET)
        exit(0)
else:
    print(Fore.LIGHTRED_EX + "DIE!!!!!" + Fore.RESET)
    exit(1)
