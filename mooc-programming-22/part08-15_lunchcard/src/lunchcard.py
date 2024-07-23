# Write your solution here:
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance
    
    def eat_lunch(self):
        if self.balance >= 2.6:
            self.balance -= 2.6
    
    def eat_special(self):
        if self.balance >= 4.6:
            self.balance -= 4.6
    
    def deposit_money(self, amount):
        if amount < 0:
            raise ValueError('You cannot deposit an amount of money less than zero')
        self.balance += amount
            
    def __str__(self):
        return f'The balance is {self.balance:.1f} euros'

def main():
    peters_card = LunchCard(20)
    # print(peters_card)
    graces_card = LunchCard(30)
    # print(graces_card)
    peters_card.eat_special()
    print(f'Peter: {peters_card}')
    graces_card.eat_lunch()
    print(f'Grace: {graces_card}')
    peters_card.deposit_money(20)
    print(f'Peter: {peters_card}')
    graces_card.eat_special()
    print(f'Grace: {graces_card}')
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    print(f'Peter: {peters_card}')
    graces_card.deposit_money(50)
    print(f'Grace: {graces_card}')

main()
