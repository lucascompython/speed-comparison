#!/usr/bin/env python3

import os, sys, argparse
from prettytable import PrettyTable
from colorama import Fore, Style
import matplotlib.pyplot as plt
from time import time



def arg_parser() -> None:
    parser = argparse.ArgumentParser(description="Calculate the prime numbers between any given range.")
    parser.add_argument("-c", "--custom", help="Enter two custom values.", type=int, nargs=2)
    args = parser.parse_args()
    return args


def main():
    args = vars(arg_parser())
    lower = args["custom"][0]
    upper = args["custom"][1]


main()
