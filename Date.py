"""
This module provides date-related utility functions:
- days_in_month: Returns number of days in a given month
- is_valid_date: Checks if a date is valid
- days_between: Calculates days between two dates
- age_in_days: Calculates age in days from birthdate to today
"""
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
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    if year<datetime.MINYEAR or year>datetime.MAXYEAR:
        return False
    if month<1 or month >12:
        return False
    max_day=days_in_month(year,month)
    if day<1 or day>max_day:
        return False
    return True
def days_between (year1,month1,day1,year2,month2,day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if (not is_valid_date(year1,month1,day1)) or (not is_valid_date(year2,month2,day2)):
        return 0
    date1=datetime.date(year1,month1,day1)
    date2=datetime.date(year2,month2,day2)
    if date2<date1:
        return 0
    delta=date2-date1
    return delta.days
def age_in_days(year,month,day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    if not is_valid_date(year,month,day):
        return 0
    today=datetime.date.today()
    birthday=datetime.date(year,month,day)
    if(today<birthday):
        return 0
    return days_between(year,month,day,today.year,today.month,today.day)