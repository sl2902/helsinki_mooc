# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"
    
    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents
    
    def __lt__(self, another):
        return (self._euros, self._cents) < (another._euros, another._cents)
    
    def __gt__(self, another):
        return (self._euros, self._cents) > (another._euros, another._cents)
    
    def __ne__(self, another):
        return (self._euros, self._cents) != (another._euros, another._cents)
    
    def __add__(self, another):
        euros, cents = divmod((self._euros * 100 + self._cents + another._euros * 100 + another._cents), 100)
        return Money(euros, cents)
    
    def __sub__(self, another):
        euros, cents = divmod((self._euros * 100 + self._cents - another._euros * 100 - another._cents), 100)
        if euros < 0 or cents < 0:
            raise ValueError("a negative result is not allowed")
        return Money(euros, cents)
    
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1

