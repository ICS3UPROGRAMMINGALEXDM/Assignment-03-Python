#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/25/2022
# Description: Gets 3 numbers from the user and calculates the average, uses error checking

import colorama
from colorama import Fore, Style


def calculate():
    while True:
        # Getting user input
        num1 = input(Style.BRIGHT + Fore.WHITE + "Enter your first number: ").strip()
        num2 = input("Enter your second number: ").strip()
        num3 = input("Enter your third number: ").strip()

        # Try for error checking
        try:
            # Casting to float
            num1 = float(num1)
            num2 = float(num2)
            num3 = float(num3)

            # checking to make sure that the numbers are in the correct range
            if (
                num1 >= 0
                and num1 <= 100
                and num2 >= 0
                and num2 <= 100
                and num3 >= 0
                and num3 <= 100
            ):
                # Calcualte the average
                average = (num1 + num2 + num3) / 3

                print(
                    Fore.YELLOW
                    + "The average of your three numbers is {:.2f}".format(average)
                )

                # Loop for error checking user answer if they'd like to calculate again
                while True:
                    answer = (
                        input(Fore.WHITE + "Would you like to play again? (y/n): ")
                        .lower()
                        .strip()
                    )

                    # if statement for the user answer
                    if answer == "y":
                        print(Fore.GREEN + "Okay")
                        break
                    elif answer == "n":
                        print(Fore.MAGENTA + "Okay")
                        break
                    else:
                        print(Fore.RED + "I don't understand, please try again")
            else:
                print(Fore.RED + "Please make sure your numbers are between 0-100")

            try:
                # Ends program after everythings complete and user enter "n"
                if answer == "n":
                    break
            except NameError:
                print("")

        except ValueError:
            print(Fore.RED + "Invalid input, try again!")


def main():
    calculate()


if __name__ == "__main__":
    main()
