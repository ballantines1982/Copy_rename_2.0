import datetime


def add(moment):
    """
    Return the date when a gigasecond has passed 
    """
    gigasecond = 1000000000
    return moment + datetime.timedelta(seconds = gigasecond)
