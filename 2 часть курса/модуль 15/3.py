class Date:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        day, month, year = map(int, date_str.split('-'))
        return cls(day, month, year)

    @staticmethod
    def is_date_valid(date_str: str) -> bool:
        day, month, year = map(int, date_str.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 12:
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"День: {self._day}\tМесяц: {self._month}\tГод: {self._year}"


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))