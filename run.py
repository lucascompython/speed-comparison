#!/usr/bin/env python3

import os, sys, argparse
from prettytable import PrettyTable
from colorama import Fore, Style
import matplotlib.pyplot as plt
from time import time


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def arg_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Calculate the prime numbers between any given range.")
    parser.add_argument("-c", "--custom", help="Enter two custom values.", type=int, nargs=2)
    args = parser.parse_args()
    return args


def main() -> None:

    args = vars(arg_parser())
    lower = args["custom"][0]
    upper = args["custom"][1]






if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nBye..." + Fore.RESET)
main()
