# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def weight(self):
        return self.__weight
    
    def name(self):
        return self.__name
    
    def __str__(self):
        return f'{self.__name} ({self.__weight} kg)'

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
    
    def add_item(self, item: Item):
        if item.weight() < self.__max_weight:
            self.__max_weight -= item.weight()
            self.__items.append(item)
    
    def item_size(self):
        return len(self.__items)
    
    def __str__(self):
        return f'{self.item_size()} {"item" if self.item_size() == 1 else "items"} ({ 0 if self.item_size() == 0 else self.weight()} kg)'
    
    def print_items(self):
        for item in self.__items:
            print(f'{item.name()} ({item.weight()} kg)')
    
    def weight(self):
        return sum(item.weight() for item in self.__items)
    
    def heaviest_item(self):
        heaviest_item = None
        max_weight = 0
        for item in self.__items:
            if item.weight() > max_weight:
                max_weight = item.weight()
                heaviest_item = item
        return heaviest_item

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() <= self.__max_weight:
            self.__max_weight -= suitcase.weight()
            self.__suitcases.append(suitcase)
    
    def suitcase_size(self):
        return len(self.__suitcases)
    
    # def weight(self):
    #     return sum(self.__suitcase_weights)
    
    def __str__(self):
        return f'{self.suitcase_size()} {"suitcase" if self.suitcase_size() == 1 else "suitcases"}, space for {self.__max_weight} kg'
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


if __name__ == "__main__":
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)

    # print("Name of the book:", book.name())
    # print("Weight of the book:", book.weight())

    # print("Book:", book)
    # print("Phone:", phone)
    # book.weight = 10
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(5)
    # print(suitcase)

    # suitcase.add_item(book)
    # print(suitcase)

    # suitcase.add_item(phone)
    # print(suitcase)

    # suitcase.add_item(brick)
    # print(suitcase)

    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(10)
    # suitcase.add_item(book)
    # suitcase.add_item(phone)
    # suitcase.add_item(brick)

    # print("The suitcase contains the following items:")
    # suitcase.print_items()
    # combined_weight = suitcase.weight()
    # print(f"Combined weight: {combined_weight} kg")

    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(10)
    # suitcase.add_item(book)
    # suitcase.add_item(phone)
    # suitcase.add_item(brick)

    # heaviest = suitcase.heaviest_item()
    # print(f"The heaviest item: {heaviest}")

    # cargo_hold = CargoHold(1000)
    # print(cargo_hold)

    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # adas_suitcase = Suitcase(10)
    # adas_suitcase.add_item(book)
    # adas_suitcase.add_item(phone)

    # peters_suitcase = Suitcase(10)
    # peters_suitcase.add_item(brick)

    # cargo_hold.add_suitcase(adas_suitcase)
    # print(cargo_hold)

    # cargo_hold.add_suitcase(peters_suitcase)
    # print(cargo_hold)

    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
