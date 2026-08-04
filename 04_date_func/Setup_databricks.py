# Step 1: Install python-dateutil in VS Code

# Open the VS Code terminal:

# Terminal → New Terminal

# Run:

# pip install python-dateutil

# You should see something like:

# Successfully installed python-dateutil

# Now test:

# from dateutil.relativedelta import relativedelta

# print("Works!")

# import sys

# print(sys.executable)



from datetime import datetime
from dateutil.relativedelta import relativedelta


today = datetime.today()
today = today.date()

previous_month = today - relativedelta(months=1)

print(previous_month)