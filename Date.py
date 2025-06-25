import datetime
def days_in_month(year,month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        if (year % 400 ==0) or (year % 4 == 0 and year % 100 !=0):
            return 29
        else:
            return 28
def is_valid_date (year,month,day):
    if year<=datetime.MINYEAR or year>=datetime.MAXYEAR:
        return False
    if month<1 or month >12:
        return False
    max_day=days_in_month(year,month)
    if day<1 or day>max_day:
        return False
    return True
def days_between (year1,month1,day1,year2,month2,day2):
    if (not is_valid_date(year1,month1,day1)) or (not is_valid_date(year2,month2,day2)):
        return 0
    date1=datetime.date(year1,month1,day1)
    date2=datetime.date(year2,month2,day2)
    if date2<date1:
        return 0
    delta=date2-date1
    return delta.days
def age_in_days(year,month,day):
    if not is_valid_date(year,month,day):
        return 0
    today=datetime.date.today()
    birthday=datetime.date(year,month,day)
    if(today<birthday):
        return 0
    return days_between(year,month,day,today.year,today.month,today.day)