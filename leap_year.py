#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 30, 2023
# This is a dating program for someone's grandchild


def main():
    # get the user's age
    print("In this game, I will see if you are old enough to date my grandchild.")
    user_year_string = input("What is your age: ")

    try:
        # convert user age to an integer
        user_year_int = int(user_year_string)
        # if the user is less than 0 or greater than 120, they are not a valid age

        if user_year_int % 4 == 0:
            if user_year_int % 100 == 0:
                if user_year_int % 400 == 0:
                    print("It is a leap year")
                else:
                    print("It is not a leap year")
            else:
                print("It is a leap year")
        else:
            print("It is not a leap year.")

    except:
        # if user age cannot become an integer, then tell the user to enter an integer.
        print(
            "\n{} is not a valid year. Please enter a positive integer.".format(
                user_year_string
            )
        )


if __name__ == "__main__":
    main()
