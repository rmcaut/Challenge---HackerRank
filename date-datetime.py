import os
import random
import re
import sys
from datetime import date, datetime, timedelta, timezone, time

# Complete the time_delta function below.
# *datetime.strptime()** does not convert to seconds. It parses a string into a datetime object, 
# which represents a full date and time (optionally with timezone), not a number of seconds.

def time_delta(t1, t2):
    dt1 = datetime.strptime(t1, "%d %b %Y %H:%M:%S %z")   # e.g. 15 Sep 2025 14:32:10 +0000
    dt2 = datetime.strptime(t2, "%d %b %Y %H:%M:%S %z")
    return str(int(abs((dt1 - dt2).total_seconds())))  

if __name__ == '__main__':
    t1 = input()
    t2 = input()
    delta = time_delta(t1, t2)    # <class 'str'>
    print(delta)
    print(type(delta))

    # Convert to Hours: Minutes:Seconds
    delta = int(delta)
    hours = delta // 3600
    minutes = (delta % 3600) // 60
    seconds = (delta % 60) 
    print(f'{hours:02} : {minutes:02} : {seconds:02}')
