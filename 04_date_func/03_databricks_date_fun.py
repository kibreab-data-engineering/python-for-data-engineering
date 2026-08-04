# One week report last 7 days 
from datetime import datetime, timedelta
today = datetime.today()

start_date = today - timedelta(days=7)
end_date = today

print(f" Start Date : {start_date.date()}")
print(f" End Date   :  {end_date.date()}")


# today = datetime.today()

# yesterday = today - timedelta(days=1)

# last_7_days = today - timedelta(days=7)

# last_30_days = today - timedelta(days=30)