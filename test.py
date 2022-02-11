""" Used to test code """

from datetime import datetime
from print import green_string, red_string


nowdate = datetime.now()

def days_to_new_season():
    """ Test """
    futuredate = datetime.strptime('Mar 18 2022  00:00', '%b %d %Y %H:%M')
    count = int((futuredate-nowdate).total_seconds())
    days = count//86400
    number_of_days = "{} days".format(days)
    if days == 0:
        return green_string("The F1 2022 seasons has started!".center(80))
    else:
        return red_string(f"Days left until F1 2022 Season: {number_of_days}".center(80))

days_to_new_season()