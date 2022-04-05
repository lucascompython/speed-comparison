#!/usr/bin/env python3

import os, sys, argparse
from time import time
from subprocess import check_call, STDOUT
from tempfile import NamedTemporaryFile

from prettytable import PrettyTable
from colorama import Fore, Style
import matplotlib.pyplot as plt

with open("./src/rounds.txt", "r") as f:
    ROUNDS = int(f.read())

languages = {
    "Python": "python3 main.py",
    "C++": "g++ main.cpp -o main && ./main",
}


languages_results = {}



def cleanup() -> None:
    pass


def change_round() -> None:
    with open("./src/rounds.txt", "w") as f:
        f.write(str(ROUNDS))



def name_to_abbr(reverse: bool = True, languages: dict[str, str] | list[str] = languages, capitalize: bool = False) -> dict[str, str] | list[str]:
    languages_type = type(languages)
    #checking if dict and if so convert to list
    if languages_type == dict:
        languages_values = languages.values()
        languages = languages.keys()


    new_languages = []
    #abbreviation to normal
    if reverse:
        for language in languages:
            match language.lower():
                case "c#":
                    new_languages.append("csharp")
                case "c++":
                    new_languages.append("cpp")
                case _:
                    new_languages.append(language.lower())


    #normal to abbreviation
    else:
        for language in languages:
            match language.lower():
                case "csharp":
                    new_languages.append("c#")
                case "cpp":
                    new_languages.append("c++")
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













def call_languages() -> None:
    global languages_output
    languages = name_to_abbr()

    for language, command in languages.items():
        #fast asf refer: https://stackoverflow.com/questions/13835055/python-subprocess-check-output-much-slower-then-call
        with NamedTemporaryFile() as f:
            #TODO remove shell=True and the extra sh
            check_call(f'/usr/bin/time -f " %e %P %M" sh -c  "{command}" ', shell=True, stdout=f, stderr=STDOUT, cwd="./src/" + language)
            f.seek(0)
            output = f.read().decode("utf8").split()
            #get the compilation time 
            output[2] = float(output[2]) - float(output[1])
            total_time = float(output[1]) + float(output[2])
            output.append(total_time)
        languages_results[language] = output











def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate the prime numbers between any given range.")
    parser.add_argument("-c", "--custom", help="Enter a custom rounds value.", type=int)
    parser.add_argument("-n", "--nogui", help="Use this if you don't want to use graphical graphs.", action="store_true")
    args = parser.parse_args()
    return args




def table_and_graph(total_time: float, nogui: bool) -> None:

    #table
    table = PrettyTable([
        Fore.RED + "Language" + Fore.RESET,
        Fore.GREEN + "Total time (s)" + Fore.RESET,
        Fore.BLUE + "Execution time (s)" + Fore.RESET,
        Fore.CYAN + "Compilation / Interpretation time (s)" + Fore.RESET,
        Fore.LIGHTGREEN_EX + "Peak Memory usage (kB)" + Fore.RESET,
        Fore.MAGENTA + "Version" + Fore.RESET,
    ])


    total_execution_time = 0
    total_compilation_time = 0
    total_memory_usage = 0

    for language, output in name_to_abbr(False, languages_results, True).items():
        for result in output:
            if result is output[1]:
                total_execution_time += float(result)
            elif result is output[2]:
                total_compilation_time += float(result)
            elif result is output[4]:
                total_memory_usage += int(result)
        
        table.add_row([
            language,
            round(float(output[-1]), 3),#total time
            round(float(output[1]), 3), #execution time
            round(float(output[2]), 3), #compilation time
            output[4], #memory usage
            output[0]  #version
        ])
    
    table.add_row([
        Fore.RED + f"Total ({len(languages_results)})" + Fore.RESET,
        Fore.GREEN + str(round(total_time, 3)) + Fore.RESET,
        Fore.BLUE + str(round(total_execution_time, 3)) + Fore.RESET,
        Fore.CYAN + str(round(total_compilation_time, 3)) + Fore.RESET,
        Fore.LIGHTGREEN_EX + str(total_memory_usage) + Fore.RESET,
        Fore.MAGENTA + "####" + Fore.RESET
    ])
    print(table)

    #graphs
    if not nogui:
        def graph(x: list, y: list, xlabel: str, ylabel: str, title: str, index: int) -> None:
            plt.subplot(2, 2, index)
            plt.bar(x, y)
            plt.xlabel(xlabel)
            plt.ylabel(ylabel)
            plt.title(title)
            plt.grid()



        #GUI graph
        languages = name_to_abbr(False, list(languages_results.keys()), True)

        #total time
        total_time_language = list(map(lambda x: round(x[:][-1], 3), list(languages_results.values())))
        graph(languages, total_time_language, "Languages", "Time (s)", "Total time per language", 1)

        #execution time
        execution_time_language = list(map(lambda x: round(float(x[:][1]), 3), list(languages_results.values()))) 
        graph(languages, execution_time_language, "Languages", "Time (s)", "Execution time per language", 2)

        #compilation / interpretation time
        compilation_time_language = list(map(lambda x: round(float(x[:][2]), 3), list(languages_results.values())))
        graph(languages, compilation_time_language, "Languages", "Time (s)", "Compilation / Interpretation time per language", 3)

        #memory usage
        memory_language = list(map(lambda x: x[:][4], list(languages_results.values())))
        graph(languages, memory_language, "Languages", "Memory (kB)", "Peak Memory usage per language", 4)

        plt.suptitle("Graphs")
        plt.get_current_fig_manager().set_window_title("Results")
        plt.show()


def menu(nogui: bool) -> None:
    global ROUNDS
    clear()
    start_input = ""
    while (start := start_input.lower()) not in ["start", "play"] :
        if start in ["exit", "quit", "leave"]:
            raise KeyboardInterrupt
        elif start in ["options", "config"]:
            clear()
            print(f"{Fore.MAGENTA + 'Choose one of the following options to change' + Fore.RESET}:    {Fore.CYAN + '(R)ounds' + Fore.RESET}    {Fore.LIGHTCYAN_EX + '(L)anguages' + Fore.RESET}    {Fore.LIGHTGREEN_EX + '(G)raphs' + Fore.RESET}    {Fore.RED + '(B)ack' + Fore.RESET}")
            options_input = input(f"{Fore.BLUE}options{Fore.RESET}> ")
            options_input = options_input.lower()
            #TODO add options to languages and graphs
            #rounds
            if options_input in ["rounds", "round", "r"]:
                clear()
                print("The current Rounds are set to: " + Fore.LIGHTCYAN_EX + str(ROUNDS) + Fore.RESET)
                rounds_input = input(f"{Fore.BLUE}options{Fore.RESET}/{Fore.CYAN}rounds{Fore.RESET}> ")
                if rounds_input.isdigit():
                    ROUNDS = int(rounds_input)
                    print(f"{Fore.GREEN}Rounds set to {ROUNDS}." + Fore.RESET)
            
            elif options_input in ["language", "languages", "l"]:
                pass
            elif options_input in ["graph", "graphs", "g"]:
                pass


        elif start in ["info", "information", "details"]:
            print("INFORMATIONS")




        start_input = input(
            f"Enter either {Fore.RED}'start'{Fore.RESET} to start the speed comparison, {Fore.BLUE}'options'{Fore.RESET} to change the default config, {Fore.GREEN}'info'{Fore.RESET} for the current program information or {Fore.MAGENTA}'quit'{Fore.RESET} to exit.\n->"
        )


        #if none of the above
        clear()
    change_round()
    print(f"This comparison will run to {Fore.RED + str(ROUNDS) + Fore.RESET} and it is using {Style.BRIGHT + str(len(languages.keys())) + Style.RESET_ALL} languages: {Fore.MAGENTA + ', '.join(map(str, languages.keys())) + Fore.RESET}")


    #start actual benchmark
    start_benchmark = time()
    call_languages()
    total_benchmark = time() - start_benchmark
    table_and_graph(total_benchmark, nogui)





def main() -> None:
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
