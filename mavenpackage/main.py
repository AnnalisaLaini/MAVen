pip install python-holidayapi

import requests
import json

HOLIDAYS_URL = 'https://holidayapi.com/v1/holidays?'

import holidayapi
key = '17d40907-3898-4e39-8c10-a6a9bbeb0bd1'
hapi = holidayapi.v1(key)
holidays = hapi.holidays({
  'country': 'IT',
  'year': '2021',
})

'''
Implementation of methods to deal with a calendar that lists holidays
'''



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

