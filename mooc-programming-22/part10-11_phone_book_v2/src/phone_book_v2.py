
# Write your solution here:
class Person:
    def __init__(self, name: str):
        self._name = name
        self._numbers = []
        self._address = None
    
    def add_number(self, number: str):
        self._numbers.append(number)
    
    def add_address(self, address: str):
        self._address = address
    
    def name(self):
        return self._name
    
    def numbers(self):
        return self._numbers
    
    def address(self):
        return self._address
    
    # def __str__(self):
    #     if self.name:
    #         return f'{self.name}'
    #     elif self.numbers:
    #         return f'{self.numbers}'
    #     elif self.address:
    #         return f'{self.address}'

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)
    
    def add_address(self, name: str, address: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name].numbers(), self.__persons[name].address()

    def all_entries(self):
        return self.__persons

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)
    
    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        res = self.__phonebook.get_entry(name)
        if res == None:
            print("address unknown")
            print("number unknown")  
        elif len(res[0]) == 0:
            print("number unknown")
            print(res[1])
        elif res[1] is None:
            for number in res[0]:
                print(number) 
            print("address unknown")
        else:
            for number in res[0]:
                print(number) 
            print(res[1])     

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()

# person = Person("Eric")
# print(person.name())
# print(person.numbers())
# print(person.address())
# person.add_number("040-123456")
# person.add_address("Mannerheimintie 10 Helsinki")
# print(person.numbers())
# print(person.address())
