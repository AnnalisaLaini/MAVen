import argparse
import return_event
import italianceleb
import leapyear
import weekday
import countdown

def parsing_input():

    parser = argparse.ArgumentParser(description="The program works with dates and italian holidays.\
                                                 Please insert dates in the yyyy-mm-dd format and, if the name of an\
                                                 holiday contains spaces, wrap the name around quotes ("")")


    parser.add_argument("--date",
                        help="Date for which you want to know if there is an event.\
                             Please insert the date in the yyyy-mm-dd format.")


    parser.add_argument("--holiname",
                        help="Name of the holiday to know if it is an italian celebration or not.\
                             If the name of the holiday contains spaces, please wrap it around quotes ("")")

    parser.add_argument("--year",
                        help="Enter a year to know if it is a leap year or not.")

    parser.add_argument("--wday",
                        help="Enter a date to know the corresponding weekday. \
                             Please insert the date in the yyyy-mm-dd format.")

    parser.add_argument("--todate",
                        help="Enter a date to know the countdown")


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

# python3 main.py -h
# python3 main.py --date 2021-01-01
# python3 main.py --date 2021-12-25
# python3 main.py --holiname "Christmas Day"
# python3 main.py --year 2022
# python3 main.py --wday 2022-02-12
# python3 main.py --todate 2022-02-12
