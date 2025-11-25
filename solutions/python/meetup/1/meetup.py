import calendar
import datetime


# subclassing the built-in ValueError to create MeetupDayException
class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


DOW = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}


def meetup(year, month, week, day_of_week):
    days = [
        i[DOW[day_of_week]] for i in calendar.monthcalendar(year, month)
        if i[DOW[day_of_week]] != 0
    ]
    day = 0

    if week == '1st':
        day = days[0]
    elif week == '2nd':
        day = days[1]
    elif week == '3rd':
        day = days[2]
    elif week == '4th':
        day = days[3]
    elif week == 'teenth':
        days = [i for i in days if 13 <= i <= 19]
        day = days[-1]
    elif week == '5th':
        if len(days) > 4:
            day = days[4]
        else:
            raise MeetupDayException('That day does not exist.')
    elif week == 'last':
        day = days[-1]

    return datetime.date(year, month, day)
