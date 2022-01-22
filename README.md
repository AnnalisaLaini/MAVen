# MAVen
 Lab of Software Project Development

### Dear reader, MAVen team is pleased to welcome you to our project! This is a group assignment for the final exam of Lab of SPD, a course attended by H-Farm BSc third-year students.

The MAVen package folder in this GitHub repository contains a series of files, each of them corresponding to a functionality to apply to the Calendarific API. The way each file has to be interpreted, i.e. its usage, is illustrated below.
👋🏻 welcome.py 👋🏻  The welcome function welcomes the user as soon as he/she accesses the software: a welcoming message, followed by the list of all the events that the software knows, is returned.
🥂 return event.py 🥂 The return_event function is used to return an event associated with a given date. Precisely, the user has to provide a valid calendar date in the DD-MM-YYYY format, in turn for the celebration that occurs in that specific time. By “valid calendar date”, the software means a date selected among the ones contained in the dtvnt list.
🗓 weekday.py 🗓 The weekday function returns the name of the day corresponding to the date inputted by the user. 
🎊 leap year.py 🎊 The leapyear function allows the user to know whether a year is a leap one or not. 
🤌🏻 italian celeb.py 🤌🏻 The italianceleb function allows the user to know whether an event is an Italian holiday or not. In practice, the user has to provide a valid holiday name and, in turn, the function will tell whether Italians celebrate it or not. As explained for the return_event function, by “valid holiday name” the software means a holiday name that is present in the dtvnt list.
⏰ countdown.py ⏰ The countdown function returns the number of days between the inputted date and the current date. 
The 📚 testpackage 📚 folder - within the mavenpackage folder - is a collection of files, each of them containing tests for a specific function. By running “python3 -m unittest -v -b mavenpackage/testpackage/test_*NameOfTheFunction*.py” in the terminal, the test can be executed.
Furthermore, it is possible to run a 🖇 Python style module 🖇 to assess the compliance of the project with Python PEP8 standards. To do so, it is required to run “pycodestyle filename.py” in the terminal. 
