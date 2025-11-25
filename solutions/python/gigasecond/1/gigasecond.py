"""
Given a moment, determine the moment that would be after a gigasecond has passed.
A gigasecond is 10^9 (1,000,000,000) seconds.
"""

import datetime


def add(moment):
    """

    :param moment: datetime The moment to add a gigasecond
    :return: datetime - The moment after a gigasecond has passed
    """
    return moment + datetime.timedelta(seconds=10**9)
