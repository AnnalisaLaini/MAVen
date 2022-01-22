
from holidaysimport import dtvnt


'''
The return_event function is used to infer events associated with given dates.
Provided some valid calendar date, it returns the corresponding holiday.
NOTE: The input dates need to be selected among some known entries.
The dtvnt list of holidays is used to verify the presence/absence of an entry.
The function can only return events that occur on dtvnt dates.
'''


def return_event(date):
    # First, the presence of the date in the list of
    # known occurrences is checked.
    # If the input date is included in the dtvnt list,
    # the matched event is returned.
    if date in dtvnt:
        return'{} is {}.'.format(date, dtvnt[date])

    # If the input date is not included in the dtvnt list,
    # no event is returned.
    # Instead, an apologizing message appears.
    else:
        return "Sadly, we don\'t know what is celebrated on {}".format(date)
