# import datetime library
from datetime import datetime
print("sthg")

now = datetime.now()

# current_year = now.year
current_year = datetime.now().year
current_month = now.month
current_day = now.day
current_second = datetime.now().second
print("------------------------------------")

print(now)
print("now is " + str(now))
print(current_year)
print("current_year is " + str(current_year))
print(current_month)
print("current_month is " + str(current_month))
print(current_day)
print("current_day is " + str(current_day))
print(current_second)

# DATE FORMAT = SUBSTITUTION
print("%02d-%02d-%02d-%04d"%(current_month, current_day, current_second, current_year))
print("%02d-%02d-%02d-%04d/ %02d"%(current_month, current_day, current_second, current_year, now.minute))
