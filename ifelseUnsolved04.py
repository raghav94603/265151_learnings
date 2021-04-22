year = int(input("Enter a year: "))
# Check For Leap Year because of February Month
if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

month = int(input("Enter the month : "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_days = 31
elif month == 2:
    if leap_year:
        month_days = 29
    else:
        month_days = 28
else:
    month_days = 30


day = int(input("Enter the Day : "))

if day < month_days:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [yyyy-mm-dd] %d-%d-%d." % (year, month, day))
