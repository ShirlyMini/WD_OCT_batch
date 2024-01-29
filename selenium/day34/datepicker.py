import datetime

#December 29, 2023 9:39 AM
#https://docs.python.org/3.11/library/datetime.html#datetime.date.strftime
cur_time=datetime.datetime.now()
# print(cur_time.strftime("%m %d %Y %H %S %p"))
print(cur_time.strftime("%B %d, %Y %H:%M %p"))
# year month date hour min sec millisec
spec_time=datetime.datetime(2023, 3, 12,23, 23,40,2)
print(spec_time.strftime("%B %d, %Y %H:%M:%S:%f %p"))

year=spec_time.strftime("%Y")
date=spec_time.strftime("%d").lstrip("0")
month=spec_time.strftime("%B")
hour=spec_time.strftime("%H").lstrip("0")
sec=spec_time.strftime("%S")
time_eq=spec_time.strftime("%p")
print(f"{month} {date}, {year} {hour}:{sec} {time_eq}")

