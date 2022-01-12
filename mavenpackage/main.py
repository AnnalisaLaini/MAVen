from holidaysimport.py import holidays_df
import argparse


‘ ‘ ‘ 
the welcome function is an automated function that prints a welcome message when the user opens the program
‘ ‘ ‘ 

def welcome():
    #we define the message and we associate the list of the events known by the software. We list those through the use of a dictionary.
    print("Welcome to 'Holidays Project\'. We know the dates of the following events:")
    L = []
    for k,v in dtvnt.items():
        if v not in L:
            L.append(v)
    return L

welcome()

