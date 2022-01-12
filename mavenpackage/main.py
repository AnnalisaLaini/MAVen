from holidaysimport.py import holidays_df
import argparse
from return_event.py import return_event 
from italianceleb.py import italianceleb
from leapyear.py import leapyear
from weekday.py import weekday



'''
the welcome function is an automated function that prints a welcome message when the user opens the program
'''

def welcome():
    #we define the message and we associate the list of the events known by the software. We list those through the use of a dictionary.
    print("Welcome to 'Holidays Project\'. We know the dates of the following events:")
    L = []
    for k,v in dtvnt.items():
        if v not in L:
            L.append(v)
    return L

welcome()



'''
Argparse is here used to parse arguments to the return_event function.
Arguments are user inputs that are supposed to activate the function.
The return_event function expects one positional argument, i.e. date.
The date is a necessary entry to get the function output. 
Additionally, the user can input some other arguments.
The ‘help’ argument calls for user support in setting valid entries.
The ‘choices’ argument lists valid entries to give as an input.
'''    

# First, a list of valid entries is set. 
valid_dates = dtvnt.keys()

# Then, a function relying on the argparse module is defined. 
def parse_arguments():

# note: a description of the functionality is included.
    parser = argparse.ArgumentParser(description='A program to pass dates to the return_event function')

# positional and optional arguments are set. 
    parser.add_argument("date", help="The string of the date in the form yyyy-mm-dd", choices=valid_dates)
    args = parser.parse_args()
    return return_event(args.date)
    


'''
Now, argparse is used to parse arguments to the italianceleb function.
Arguments are user inputs that are supposed to activate the function.
The italianceleb function needs a positional argument, i.e. event name.
The holiday name is a necessary entry to get the function output. 
Additionally, the user can input some other arguments.
The ‘help’ argument calls for user support in setting valid entries.
'''

# First, a list of valid entries is set. 
itaholidays = dtvnt.values()

# Then, a function relying on the argparse module is defined. 
def parseholidays():

# note: a description of the functionality is included.
    parser = argparse.ArgumentParser(description='A program to pass holidays names to the italianceleb function')

# positional and optional arguments are set. 
    parser.add_argument("holiname", help="The string of the holiday name", choices=itaholidays)
    args = parser.parse_args()
    return italianceleb(args.date)


    
# we use argparse to parse the arguments through the leapyear function

# define a function relying on the argparse module 
def parse_leapyear():
    
    #create the parser
    parser = argparse.ArgumentParser(description='Given year returns whether it is a leapyear or not')
    
    #add the argument required
    parser.add_argument("year", type=str,  help="insert the year in yyyy format")
    
    #run the argument 
    args = parser.parse_args()
    return leapyear(args)
    
    
      
''' 
With argparse we are once again parsing the arguments to be passed to the weekday function.
With this particular function we need a positional argument which allows the user to input the desired date.
'''
#we create the parser
 parser = argparse.ArgumentParser(description='Given date returns the day of the week ')
#we add the argument required
parser.add_argument("--wday", type=str,  help="insert the date in yyyy-mm-dd format")
#we  run it
 args = parser.parse_args()
   return weekday(args)

