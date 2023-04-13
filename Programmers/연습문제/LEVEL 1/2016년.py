# LEVEL 1

import datetime

def solution(a, b):
    t = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    return t[datetime.datetime(2016, a, b).weekday()]