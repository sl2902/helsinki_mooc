# TEE RATKAISUSI TÄHÄN:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self._day = day
        self._month = month
        self._year = year
    
    def __str__(self):
        return f'{self._day}.{self._month}.{self._year}'
    
    def _days_conversion(self):
        return self._day + self._month * 30 + self._year * 360
    
    def _date_conversion(self, days: int):
        year, month = divmod(days, 360)
        month, days = divmod(month, 30)
        return days, month, year
    
    def __eq__(self, another: "SimpleDate"):
        return (self._day, self._month, self._year) == (another._day, another._month, another._year)
    
    def __ne__(self, another: "SimpleDate"):
        return (self._day, self._month, self._year) != (another._day, another._month, another._year)
    
    def __lt__(self, another: "SimpleDate"):
        return (self._year, self._month, self._day) < (another._year, another._month, another._day)
    
    def __gt__(self, another: "SimpleDate"):
        return (self._year, self._month, self._day) > (another._year, another._month, another._day)
    
    def __add__(self, days: int):
        day, month, year = self._date_conversion(self._days_conversion() + days)
        return SimpleDate(day, month, year)
    
    def __sub__(self, another: "SimpleDate"):
        day, month, year = self._date_conversion(self._days_conversion() - another._days_conversion())
        diff = day + month * 30 + year * 360
        return abs(diff)

if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
    


