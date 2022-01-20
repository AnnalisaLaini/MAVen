'''
The function leapyear, as the name suggests, is used to realize
whether a year is a leapyear or not. Given the input, a year
(hence an integer), the function returns "It’s a leap year" or
"It’s not a leap year".

NOTE: The input year doesn't need to be selected among the years
present in the dtvnt's list; it can be any year.

REMEMBER: A leap year is a calendar year that contains an
additional day added to keep the calendar year synchronized with
the astronomical year. To be a leap year, the year number must be
divisible by four – except for end-of-century years, which must be
divisible by 400.
'''


import datetime


def leapyear(year):
    # year divided by 4 is a leapyear
    if (year % 4) == 0:
        # year divided by 100 means it is a century year
        if (year % 100) == 0:
            # century year divided by 400 is a leap year
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


year = input("Enter the year: ")

isValidDate = True
try:
    year = datetime.datetime(int(year), 1, 1).year
except ValueError:
    isValidDate = False
    print("Input date is not valid")

if (isValidDate):
    # Input the year in the function and print the output
    if(leapyear(year)):
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))
