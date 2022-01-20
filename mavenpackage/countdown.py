'''
Given a date inputted by the user, the countdown function returns the number of
days left to that given date (if it is a future date) or the number of days
that have passed since that date (if it is a past date)
'''


import datetime


def countdown(date_str):
    # We import the date class from the datetime module and we used the
    # date.today() method to get the current local date
    today = datetime.date.today()

    try:
        date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return "Incorrect data format, should be YYYY-MM-DD"

    # We transform the string inputted by the user to a datetime object
    # and we consider only the date part
    date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

    # We compute the difference in days between the date inputted by the user
    # and the current local date
    diff = (date_obj - today).days

    # We create different cases
    if diff > 0:
        # If the difference is bigger than 0, we print the number of days left
        return "Time left: {} days".format(diff)

    elif diff == 0:
        # If the difference is equal to 0, we say to the user that the input
        # date is the current date
        return "Time left: {} days!\
        The date you input refers to today".format(diff)

    elif diff < 0:
        # If the difference is smaller than 0, we take the absolute value of
        # the difference in days and we print the number of days passed since
        # that day
        diff = abs(diff)
        return "{} days have passed since the input date".format(diff)
