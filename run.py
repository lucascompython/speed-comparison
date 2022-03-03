#!/usr/bin/env python3

import os, sys, argparse
from prettytable import PrettyTable
from colorama import Fore, Style
import matplotlib.pyplot as plt
from time import time


lower = 1
upper = 100_000

languages = {
    "Python": "python3 main.py"
}



def call_languages():
    pass




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
    while not (start := start_input.lower()) in ["start", "play"] :
        start_input = input(
            f"Enter {Fore.RED}'start'{Fore.RESET} to start the speed comparison or {Fore.BLUE}'options'{Fore.RESET}.\n->"
        )

        if start == "options":
            clear()
            options_input = input(f"/{Fore.BLUE}options{Fore.RESET}> ")


        elif start == "info":
            print("INFORMATIONS")
    print(f"This comparison will running between {Fore.RED + str(lower) + Fore.RESET} and {Fore.RED + str(upper) + Fore.RESET} and it is using {Style.BRIGHT + str(len(languages.keys())) + Style.RESET_ALL} languages: {', '.join(map(str, languages.keys()))}")






def main() -> None:

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
