# WRITE YOUR SOLUTION HERE:
class BankAccount:
    def __init__(self, name: str, account_number: str, amount: float):
        self.__name = name
        self.__account_number = account_number
        self.__balance = amount
    
    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError("Amount {amount} cannot be negative")
        self.__balance += amount
        self.__service_charge()
    
    def withdraw(self, amount: float):
        if amount > self.__balance:
            raise ValueError("Insufficient balance. Cannot make withdrawal")
        self.__balance -= amount
        self.__service_charge()
    
    def __service_charge(self):
        self.__balance *= 0.99
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount: float):
        if amount >= 0:
            self.__balance = amount

if __name__ == "__main__":
    account = BankAccount("Randy Riches", "12345-6789", 1000)
    account.withdraw(100)
    print(account.balance)
    account.deposit(100)
    print(account.balance)


