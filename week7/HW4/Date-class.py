from datetime import date
import jdatetime
import hijridate


months = [None, 'January', 'February','March', 'April' , 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
months_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}


class Date:
    def __init__(self, year, month, day) -> None:
        assert isinstance(year, int) and 0 < year <= 9999, "Year must be between 0 and 9999"
        self.year = year
        assert isinstance(month, int) and 0 < month <= 12, "Months must be between 0 and 13"
        self.month = month
        assert isinstance(day, int) and day <= months_days[months[month]]
        self.day = day
        self.date = date(self.year, self.month, self.day)

    @classmethod
    def from_string(cls, date_string: str): # handle ISO format YYYY-MM-DD
        my_date = date.fromisoformat(date_string)
        return cls(my_date.year, my_date.month, my_date.day)

    @classmethod
    def from_ordinal(cls, days: int): # handle Ordinal format(days from beginnig of the date)
        assert isinstance(days, int) and 0 < days <= 3652059, "Days must be an integer between 0 and 3652060"
        the_date = date.fromordinal(days)
        return cls(the_date.year, the_date.month, the_date.day)

    @classmethod
    def from_timestamp(cls, time: int):
        assert isinstance(time, int)
        the_date = date.fromtimestamp(time)
        return cls(the_date.year, the_date.month, the_date.day)

    @staticmethod
    def is_valid_date(a_date):
        assert date.fromisoformat(a_date), f"the given date is not a valid date! expected format is YYYY-MM-DD"
        return True

    def to_shamsi(self):
        jalali_date = jdatetime.date.fromgregorian(year=self.year, month=self.month, day=self.day)
        return jalali_date
        # shamsi_days = date.toordinal(self.date) - 226_870
        # shamsi_year = shamsi_days // 365
        # shamsi_month =((shamsi_days % 365) // 30.416666666666668)+1
        # shamsi_day = ((shamsi_days % 365) % 30.416666666666668)
        # return f"{shamsi_year}-{shamsi_month}-{shamsi_day}"

    def to_ghamari(self):
        hijri_date = hijridate.Gregorian(self.year, self.month, self.day).to_hijri()
        return hijri_date


# non_valid_date = Date.is_valid_date(str(date.today()))
# print(non_valid_date)
date1 = Date.from_string("2021-01-21")
print(date1.to_shamsi())
