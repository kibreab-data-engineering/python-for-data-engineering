# Lesson 2 - Date Arithmetic with timedelta

# datetime → Gets the current date and time.
# timedelta → Adds or subtracts time.
'''
from datetime import datetime, timedelta
today = datetime.today()
print(today.date())

'''

from datetime import datetime, timedelta
today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(days=7)
last_30_days = today - timedelta(days=30)
print("=================================================")
print(f" Yeasterday :  {yesterday.date()}")
print(f" Tomorrow :    {tomorrow.date()}")
print(f" last week 7 days ago {last_week.date()}")
print(f" last week 30 days ago {last_30_days.date()}")
print("=================================================")


