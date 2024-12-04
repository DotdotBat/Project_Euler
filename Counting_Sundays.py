import numpy
print("hello Euler")

months_day_number = []
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.

# All the rest have thirty-one,
months_day_number = numpy.full(shape=(12), fill_value=31)
# Thirty days has September,
# April, June and November.
month_numbers_with_30_days = [9,3,6,11]
for i in month_numbers_with_30_days:
    months_day_number[i-1] = 30
del month_numbers_with_30_days
# Saving February alone,
# Which has twenty-eight, rain or shine.
months_day_number[2-1] = 28

def is_leap_year(year_number:int):
    """A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400."""
    y = year_number
    not_leap = y%4!=0 or (y%100==0 and y%400!=0) 
    # print(y%4!=0, y%100==0, y%400!=0, not_leap)
    return (not not_leap)




print("months_day_number:", months_day_number)
print("is a leap year?")
print("3", is_leap_year(3))
print("4", is_leap_year(4))
print("100", is_leap_year(100))
print("400", is_leap_year(400))

def days_in_this_month(year:int, month:int):
    number = months_day_number[month-1]
    if number == 28 and is_leap_year(year):
        return 29
    return number
print(days_in_this_month(year=800, month=2))

def turn_calendar_page():
    global week_day, day_of_month, month, year
    week_day+=1
    if week_day>7: week_day=1
    day_of_month+=1
    
    if day_of_month > days_in_this_month(year, month):
        month+=1
        day_of_month = 1
    
    if month>12:
        year+=1
        month = 1


#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#1 Jan 1901
year = 1901
month = 1
day_of_month = 1
week_day = 1

print(year, month, day_of_month, week_day)
turn_calendar_page()
print(year, month, day_of_month, week_day)


# 31 Dec 2000
end_year = 2000
end_month = 12
end_day = 31

sunday_on_1st_count = 0
while(year<=end_year):
    if day_of_month == 1 and week_day ==7:
        sunday_on_1st_count+=1
    turn_calendar_page()
    
print(year, month, day_of_month, week_day)
print(sunday_on_1st_count)