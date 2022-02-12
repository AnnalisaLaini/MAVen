'''
THIS MODULE IS MEANT TO IMPORT HOLIDAYS DATA FROM
CALENDARIFIC API AND TURN IT INTO CSV FORMAT.
'''


import pandas as pd

holidays_df = pd.read_csv('holiday.csv')
# print(holidays_df)

holidays_df = holidays_df.drop(["country", "year"], axis=1)
# print(holidays_df)

date_event = holidays_df[["ds", "holiday"]]
# date_event

dates_list = date_event["ds"]
events_list = date_event["holiday"]

dtvnt = dict(zip(date_event.ds, date_event.holiday))
# print(dtvnt)