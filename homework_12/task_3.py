"""
Сгенерировать список четных дат на текущий месяц.
Можно использовать тот пример task_3_1 а можно чуть подумать и сделать проще.
"""


from datetime import datetime

month = datetime.now().month
year = datetime.now().year

days_in_month = 0
even_dates = []

print(month)
print(year)


if month in (1, 3, 5, 7, 8, 10, 12):
    days_in_month = 31
elif month in (4, 6, 9, 11):
    days_in_month = 30
elif month == 2 and year % 4 == 0:
    days_in_month = 29
else:
    days_in_month = 28

even_dates = [x for x in range(1, days_in_month + 1) if x % 2 == 0]

print(even_dates)
