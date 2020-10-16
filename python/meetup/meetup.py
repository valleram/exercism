from calendar import Calendar
from datetime import date


class MeetupDayException(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def meetup(year, month, week, day_of_week):
    weekdays = {'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
    cal = Calendar()

    for i in cal.itermonthdates(year=year, month=month):
        if week == 'teenth' and 13 <= i.day < 20 and i.isoweekday() == weekdays[day_of_week]:
            return date(i.year, i.month, i.day)
        elif week == '1st' and 1 <= i.day <= 7 and i.isoweekday() == weekdays[day_of_week]:
            return date(i.year, i.month, i.day)
        elif week == '2nd' and 8 <= i.day <= 14 and i.isoweekday() == weekdays[day_of_week]:
            return date(i.year, i.month, i.day)
        elif week == '3rd' and 15 <= i.day <= 21 and i.isoweekday() == weekdays[day_of_week]:
            return date(i.year, i.month, i.day)
        elif week == '4th' and 22 <= i.day <= 28 and i.isoweekday() == weekdays[day_of_week]:
            if i.month == month:
                return date(i.year, i.month, i.day)
        elif week == '4th' and 22 <= i.day <= 28 and i.isoweekday() == weekdays[day_of_week]:
            return date(i.year, i.month, i.day)
