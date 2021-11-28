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
Lab of Sofware Project Development 2021/2022

Implementation of methods to deal with a calendar that lists holidays
''
