
## list of hours
#1st hour: 7:32-8:31
#2nd hour: 8:35-9:33
#3rd hour: 9:37-10:35
#4th hour: 10:39-12:15
#5th hour: 12:19-1:17
#6th hour: 1:21-2:19

from datetime import datetime
import datetime
import schedule
import time
import os

def display_time():
    os.system('cls' if os.name == 'nt' else 'clear')
    current_time = datetime.datetime.now().time()
    rounded_time = current_time.replace(second=0, microsecond=0)
    print("The current time is", rounded_time)

    if rounded_time >= datetime.time(7,32) and rounded_time <= datetime.time(8,31):
        print("It is 1st hour now")
    elif rounded_time >= datetime.time(8,35) and rounded_time <= datetime.time(9,33):
        print("It is 2nd hour now")
    elif rounded_time >= datetime.time(9,37) and rounded_time <= datetime.time(10,35):
        print("It is 3rd hour now")
    elif rounded_time >= datetime.time(10,39) and rounded_time <= datetime.time(12,15):
        print("It is 4th hour now")
    elif rounded_time >= datetime.time(12,19) and rounded_time <= datetime.time(13,17):
        print("It is 5th hour now")
    elif rounded_time >= datetime.time(13,21) and rounded_time <= datetime.time(14,19):
        print("It is 6th hour now")
    else:
        print("Not in school hours")

    schedule.every(30).seconds.do(display_time)
while True:
    schedule.run_pending()
    time.sleep(1)


##This code will check the current time and print out which hour it is in school. It will also update every second to keep the information current.

