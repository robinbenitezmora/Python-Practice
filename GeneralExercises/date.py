
from datetime import date

def get_date():
    today = date.today()
    return today

def get_year():
    today = date.today()
    return today.year

def get_month():
    today = date.today()
    return today.month

def get_day():
    today = date.today()
    return today.day

def get_day_name():
    today = date.today()
    return today.strftime('%A')

def get_weekday():
    today = date.today()
    return today.weekday()

def get_weekday_name():
    today = date.today()
    return today.strftime('%A')

def get_month_name():
    today = date.today()
    return today.strftime('%B')

print(f'Today is {get_day_name()}, {get_day()} of {get_month_name()} of {get_year()}')
