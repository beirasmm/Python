### Dates ###

from datetime import timedelta
from datetime import date
from datetime import time
from datetime import datetime

now = datetime.now()


def print_date(date):
    print(date.day)
    print(date.month)
    print(date.year)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())


print_date(now)

time_stamp = now.timestamp()
# today = now.today()

print(time_stamp)
# print(today)

# print(now.fromtimestamp(time_stamp, now.tzinfo))

year_2023 = datetime(2023, 1, 1, 0)

print_date(year_2023)

current_time = time(6, 25, 55)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


current_date = date.today()

print(current_date)
print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(2022, 4, 4)
print(current_date)

current_date = date(current_date.year,
                    current_date.month + 1, current_date.day)
print(current_date.month)

print(year_2023.date() - current_date)
print(year_2023 - now)
# print(year_2023.time() - current_time)

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)
print(end_timedelta - start_timedelta)
