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
    isValidDate = True
    try:
        year = datetime.datetime(int(year), 1, 1).year
    except ValueError:
        isValidDate = False
        return "Input date is not valid"

    # year divided by 100 means it is a century year
    # century year divided by 400 is a leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return "{0} is a leap year".format(year)
    
    # year divided by 4 is a leapyear
    # not divided by 100 means that it is not a century year
    elif (year % 4 == 0) and (year % 100 != 0):
        return "{0} is a leap year".format(year)

    else:
        return "{0} is not a leap year".format(year)

