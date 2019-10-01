#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: September 2019
# This is a number guessing program

import constants


def main():

    # Asking if they can guess my number that I choose between 0 and 10

    print("Can you guess the number I choose from 0 to 10?")

    # input
    number = int(input("Enter the number that you think I guessed: "))

    # process
    if (number == constants.constant_number):
        print("You guessed it :)")


if __name__ == main():
    main()
