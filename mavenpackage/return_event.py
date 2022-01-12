
def return_event(date):

    if date in dtvnt:
        print('{} is {}.'.format(date, dtvnt[date]))

    else:
        print('Sadly, we don\'t know what is celebrated on {}\.'.format(date))
