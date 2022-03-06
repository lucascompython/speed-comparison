#!/usr/bin/env python3

import os, sys, argparse
from time import time
from subprocess import check_call, STDOUT
from tempfile import NamedTemporaryFile

from prettytable import PrettyTable
from colorama import Fore, Style
import matplotlib.pyplot as plt

lower = 1
upper = 100_000

languages = {
    "Python": "python3 main.py",
}



def name_to_abbr(mode: bool = True, languages: dict[str, str] | list[str] = languages, capitalize: bool = False) -> dict[str, str] | list[str]:
    languages_type = type(languages)
    #checking if dict and if so convert to list
    if languages_type == dict:
        languages_values = languages.values()
        languages = languages.keys()


    new_languages = []
    #abbreviation to normal
    if mode:
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
        for value in languages_values:
            for language in new_languages:
                return_languages[language] = value
        return return_languages

    return new_languages













def call_languages():
    languages = name_to_abbr()
    for language, command in languages.items():
        #fast asf refer: https://stackoverflow.com/questions/13835055/python-subprocess-check-output-much-slower-then-call
        with NamedTemporaryFile() as f:
            check_call(command.split(), stdout=f, stderr=STDOUT, cwd="./src")
            f.seek(0)
            output = f.read()

    print(output)








def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate the prime numbers between any given range.")
    parser.add_argument("-c", "--custom", help="Enter two custom values.", type=int, nargs=2)
    args = parser.parse_args()
    return args



def menu(lower: int, upper: int) -> None:
    clear()
    start_input = ""
    while (start := start_input.lower()) not in ["start", "play"] :
        if start == "options":
            clear()
            options_input = input(f"/{Fore.BLUE}options{Fore.RESET}> ")

        elif start == "info":
            print("INFORMATIONS")
        start_input = input(
            f"Enter {Fore.RED}'start'{Fore.RESET} to start the speed comparison or {Fore.BLUE}'options'{Fore.RESET}.\n->"
        )


        #if none of the above
        clear()
    print(f"This comparison will running between {Fore.RED + str(lower) + Fore.RESET} and {Fore.RED + str(upper) + Fore.RESET} and it is using {Style.BRIGHT + str(len(languages.keys())) + Style.RESET_ALL} languages: {Fore.MAGENTA + ', '.join(map(str, languages.keys())) + Fore.RESET}")
    call_languages()







def main() -> None:
    global lower, upper
    if (args := arg_parser().custom):
        lower = args[0]
        upper = args[1]

    menu(lower, upper)




if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nBye..." + Fore.RESET)
        exit(0)
else:
    print(Fore.LIGHTRED_EX + "DIE!!!!!" + Fore.RESET)
    exit(1)
