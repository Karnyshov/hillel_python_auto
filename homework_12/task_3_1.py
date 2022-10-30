from datetime import date, datetime, timedelta

current_month = datetime.now().month
current_year = datetime.now().year

# work around if now the latest month in year
if current_month == 12:
    _current_year = current_year + 1
    _current_month = 1
else:
    _current_year = current_year
    _current_month = current_month

month_days = (date(_current_year, _current_month, 1) - date(current_year, current_month, 1)).days

first_date_of_month = date(current_year, current_month, 1)
last_date_of_month = date(current_year, current_month, month_days)
delta_days = last_date_of_month - first_date_of_month

dates = []

for day in range(delta_days.days + 1):
    date = first_date_of_month + timedelta(days=day)
    day_number = date.weekday()
    if day_number < 5:
        dates.append(date)
        print(date)