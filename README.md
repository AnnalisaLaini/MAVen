# MAVen Project 🗓
Lab of Software Project Development <br/>
[ET7018] LAB OF SOFTWARE PROJECT DEVELOPMENT (ET7) - a.a. 2021-22

### Dear reader, MAVen team is pleased to welcome you to our project! 
### This is a group assignment for the final exam of Lab of SPD, a course attended by H-Farm BSc third-year students.
The MAVen package folder in this GitHub repository contains a series of files, each of them corresponding to a 
functionality to apply to the holiday.csv file. The way each file has to be interpreted, i.e. its usage, is 
illustrated below.
<br/>
- 🥂 **return event.py** 🥂 : The return_event function is used to return an event associated with a given date. 
<br/>Precisely, the user has to provide a valid calendar date in the DD-MM-YYYY format, in turn for the celebration 
that occurs in that specific time. 
<br/>By “valid calendar date”, the software means a date selected among the ones contained in the dtvnt list.
- 🗓 **weekday.py** 🗓 : The weekday function returns the name of the day corresponding to the date inputted 
by the user. 
- 🎊 **leap year.py** 🎊 : The leapyear function allows the user to know whether a year is a leap one or not. 
- 🤌🏻 **italian celeb.py** 🤌🏻 : The italianceleb function allows the user to know whether an event is an Italian 
holiday or not. In practice, the user has to provide a valid holiday name and, in turn, the function will tell 
whether Italians celebrate it or not. <br/>As explained for the return_event function, by “valid holiday name” the 
software means a holiday name that is present in the dtvnt list. <br/> If the name of the holiday contains spaces, 
the user has to wrap the name around quotes (\"\") 
- ⏰ **countdown.py** ⏰ : The countdown function returns the number of days between the inputted date and the 
current date. 

> **Note:** We know the dates of the following events: <br/> - 'New Year's Day', <br/>- 'Epiphany', 
> <br/>- 'March Equinox', <br/>- 'Good Friday', <br/>- 'Easter Sunday', <br/>- 'Easter Monday', 
> <br/>- 'The Feast of St Mark (Venice)', <br/>- 'Labor Day / May Day', <br/>- 'Republic Day', <br/>- 'June Solstice', 
> <br/>- 'The Feast of St. John (Florence, Genoa, Turin)', <br/>- 'The Feast of St. Peter and St. Paul (Rome)', 
> <br/>- 'Ferragosto', <br/>- 'The Feast of Saint Januarius (Naples)', <br/>- 'September Equinox', 
> <br/>- 'All Saints' Day', <br/>- 'The Feast of St. Ambrose (Milan)', <br/>- 'Feast of the Immaculate Conception', 
> <br/>- 'December Solstice', <br/>- 'Christmas Day', <br/>- 'St. Stephen's Day', <br/>- 'New Year's Eve'

## Command line parameters 💻
 
Optional arguments:
- **--date:** it will let you enter a date to know if there is an holiday
- **--holiname:** it will let you enter the name of an holiday to know if it is an italian celebration or not
- **--year:** it will let you a year number to know if it is a leap year or not
- **--wday:** it will let you enter a date to know the corresponding weekday
- **--todate:** it will let you enter a date to know how many days are left or have passed 

Here are some examples of code and output
```
$ python3 main.py --wday 2022-02-12
The requested date is on a Saturday
```
```
$ python3 main.py --year 2020
2020 is a leap year
```
```
$ python3 main.py --date 2021-01-01
2021-01-01 is New Year's Day.
```
```
$ python3 main.py --holiname "Christmas Day"
Yup, Christmas Day is an Italian holiday!
```

## Testing & Styling ✅
The **testpackage** folder - within the mavenpackage folder - is a collection of files, each of them containing 
tests for a specific function. <br/>
By running ```python3 -m unittest -v -b mavenpackage/testpackage/test_*NameOfTheFunction*.py``` in the terminal, 
the test can be executed.

Furthermore, it is possible to run a Python style module to assess the compliance of the project with Python 
PEP8 standards. <br/>
To do so, it is required to run ```pycodestyle filename.py``` in the terminal. 

> **Note:** the project requires the following modules to run: *argparse*, *pandas*, *unittest*, *datetime*.


## Authors 👩🏻‍💻

- Martina Boni (878935)
- Annalisa Laini (878279)
- Vanessa Pozzi (879819)
- Martina Turus (878176)

Thanks for your attention!

Team MAVen












