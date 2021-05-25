"""A vaccination calculator."""

__author__ = 730429363

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
administered: int = int(input("Doses administered: "))
doses_per_day: int = int(input("Doses per day: "))
target_vaxxed: int = int(input("Target percent vaccinated: "))
vaccinations_remaining: float = float((target_vaxxed * population / 100) - (administered / 2))
days_remaining: int = round(2 * vaccinations_remaining / float(doses_per_day))
today: datetime = datetime.today()
target_date: datetime = today + timedelta(days_remaining)
print("We will reach " + str(target_vaxxed) + "% vaccination in " + str(days_remaining) + " days, which falls on " + str(target_date.strftime("%B %d, %Y")) + ".")