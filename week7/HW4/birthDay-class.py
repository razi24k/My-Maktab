import time


class BirthDay:
    year_begin = 1970
    month_begin = 1
    day_begin = 1
    hour_begin = 0

    def __init__(self, year: int, month: int, day: int, hour: int):
        self.year = year
        # self.years_sec = (year - BirthDay.year_begin) * 3.154e+7
        self.month = month
        self.months_sec = (month - BirthDay.month_begin) * (3.154e+7 / 12)
        self.day = day
        self.days_sec = (day - BirthDay.day_begin) * (3.154e+7 / 365)
        self.hour = hour
        self.hours_sec = (hour - BirthDay.hour_begin) * (3.154e+7 / (24 * 365))

    @property
    def years_sec(self):
        return (self.year - BirthDay.year_begin) * 3.154e+7

    def calculate_age(self):
        age_seconds = (self.years_sec + self.months_sec + self.days_sec + self.hours_sec)
        now = time.time()
        years_of_age = (now - age_seconds) / 3.154e+7
        months_of_age = (years_of_age % 1) * 12
        days_of_leap_years = years_of_age // 5
        days_of_age = (months_of_age % 1) * 30 - days_of_leap_years
        if days_of_age < 0:
            days_of_age = 30 - days_of_age
            months_of_age += 1
        hours_of_age = (days_of_age % 1) * 24
        return (f"your age is: {int(years_of_age)} years and {int(months_of_age)} months and "
                f"{int(days_of_age)} days and {int(hours_of_age)} hours")

    def remaining_to_birthday(self):
        age_seconds = (self.years_sec + self.months_sec + self.days_sec + self.hours_sec)
        year_remain = 1 - ((time.time() - age_seconds) / 3.154e+7) % 1
        month_remain = year_remain * 12
        days_remain = (month_remain % 1) * 30
        hour_remain = (days_remain % 1) * 24
        return (f"{int(month_remain)} months and {int(days_remain)} days and {int(hour_remain)}"
                f" hours remains to your birthday")


rasool = BirthDay(1999, 9, 30, 21)
print(rasool.calculate_age())
print(rasool.remaining_to_birthday())
