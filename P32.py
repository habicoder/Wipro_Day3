'''

Exercise 9: Generate a random date between given start and end dates

'''
import random
from datetime import datetime, timedelta

def random_date(start_date, end_date):
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d')
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d')
    
    delta = end_datetime - start_datetime
    
    random_days = random.randint(0, delta.days)
    
    random_date = start_datetime + timedelta(days=random_days)
    
    return random_date.strftime('%Y-%m-%d')

start_date = '2024-01-01'
end_date = '2024-12-31'
random_date = random_date(start_date, end_date)
print("Random date between", start_date, "and", end_date, ":", random_date)