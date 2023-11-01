#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 31, 2023
# // This a program that displays indicates which years are leap years


def main():
    # get the user year as a string
    print("This program displays whether the year entered is a leap year or not.")
    user_year_string = input("Enter a year: ")

    try:
        # convert user year to an integer
        user_year_int = int(user_year_string)

        # if the user year is divisible by 4, then see if it is divisible by 100
        if user_year_int % 4 == 0:
            # if the user year is divisible by 100, then see if it is divisible by 400
            if user_year_int % 100 == 0:
                # if the user year is divisible by 400, then the year is a leap year.
                if user_year_int % 400 == 0:
                    print("It is a leap year")
                else:
                    # otherwise, the year is not a leap year
                    print("It is not a leap year")
            else:
                # otherwise, the year iS a leap year
                print("It is a leap year")
        else:
            # otherwise, the year is not a leap year
            print("It is not a leap year.")

    except:
        # if the year is not an integer, then tell them their input is invalid
        print(
            "\n{} is not a valid year. Please enter a positive integer.".format(
                user_year_string
            )
        )


if __name__ == "__main__":
    main()
