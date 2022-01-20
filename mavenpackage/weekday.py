'''
The weekday function returns the day’s name, given the date inputted
by the user
'''

import datetime


def weekday(date_str):
    # We define a list with the days of the week
    weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday", "Sunday")
    # We transform the string to a datetime object
    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return
    # weekday() returns the day of the week as an integer number,
    # where Monday is 0 and Sunday is 6
    date_obj_day = date_obj.weekday()
    # We associate the given integer with the name taken from the weekDays
    # list we had created previously
    day_of_the_week = weekDays[date_obj_day]
    # We print the outcome
    print("The requested date is on a {}".format(day_of_the_week))
