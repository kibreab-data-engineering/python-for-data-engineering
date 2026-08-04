# For previous month calculations, timedelta is not enough because months have different numbers of days.

# Example:

# January - 31 days
# February - 28/29 days
# March - 31 days

# We will use:

# # from dateutil.relativedelta import relativedelta

# calculate previous month 
'''
from datetime import datetime

today = datetime(2026,1,15)

if today.month == 1:
    previous_month = 12 
    previous_year = today.year - 1
else:
    previous_month = today.month - 1
    previous_year = today.year - 1

print(f"Previous Month:  {previous_month}")
print(f"Previous Year: {previous_year}")


from datetime import datetime, timedelta

today = datetime.today()
previous_month_start = (today - timedelta(days=-1))
print(previous_month_start)

'''
