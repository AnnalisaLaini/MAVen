

from holidaysimport import dtvnt

'''
The italianceleb function tells whether an event is or not an Italian holiday.
Provided some valid holiday names, it tells if Italians celebrate them.
NOTE: The holidays celebrated by Italians are those in the dtvnt dict.
The dtvnt dictionary lists Italian holidays as values.
The function checks for events’ presence in the dtvnt values.
If an input event is present, then it is considered as an Italian holiday.
Otherwise, the function does not recognize it as such.
'''


def italianceleb(someholi):
    if someholi in dtvnt.values():
        print("Yup, {} is an Italian holiday!".format(someholi))
    else:
        print("Nope, Italians do not celebrate {}.".format(someholi))
