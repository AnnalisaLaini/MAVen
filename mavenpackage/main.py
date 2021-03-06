import argparse
import return_event
import italianceleb
import leapyear
import weekday
import countdown


def parsing_input():

    parser = argparse.ArgumentParser(description="The program works with\
     dates and italian holidays.\
     Please insert dates in the yyyy-mm-dd format and,\
     if the name of a\
     holiday contains spaces, wrap the name around quotes (\"\")")

    parser.add_argument("--date",
                        help="Enter a date for which you want\
                        to know if there is an event.\
                        Please insert the date in the\
                        yyyy-mm-dd format.")

    parser.add_argument("--holiname",
                        help="Enter the name of an holiday to know\
                        if it is an italian celebration or not.\
                        If the name of the holiday contains spaces,\
                        please wrap it around quotes (\"\")")

    parser.add_argument("--year",
                        help="Enter a year to know if it is a leap\
                        year or not.")

    parser.add_argument("--wday",
                        help="Enter a date to know the corresponding\
                        weekday. \
                        Please insert the date in the yyyy-mm-dd format.")

    parser.add_argument("--todate",
                        help="Enter a date to know the countdown. \
                        Please insert the date in the yyyy-mm-dd format.")

    args = parser.parse_args()

    date = args.date
    holiday = args.holiname
    year = args.year
    dayoftheweek = args.wday
    countd = args.todate

    if args.date:
        print(return_event.return_event(args.date))

    elif args.holiname:
        print(italianceleb.italianceleb(holiday))

    elif args.year:
        print(leapyear.leapyear(year))

    elif args.wday:
        print(weekday.weekday(dayoftheweek))

    elif args.todate:
        print(countdown.countdown(countd))


parsing_input()

