#!/usr/bin/env python3

# Created by: Dylan Melo
# Created on: January 2022
# This program uses a nested loop to display a 0-9 multiplication table.

import colorama
from colorama import Fore
from colorama import Style


def main():
    # this function uses a nested loop

    counter1 = 10
    counter2 = 1
    # process & output
    print(Fore.YELLOW + "Hello, welcome to Dylan's multiplication table")
    for counter1 in range(10):
        for counter2 in range(10):
            prdct = counter1*counter2
            print(Fore.RED + "{0}x{1} = {2}".format(counter1, counter2, prdct))


if __name__ == "__main__":
    main()
