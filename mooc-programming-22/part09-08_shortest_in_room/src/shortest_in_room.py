# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def print_contents(self):
        print(f'There are {len(self.persons)} in the room, and their combined height is {sum(person.height for person in self.persons)} cm')
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')
    
    def shortest(self):
        min_height = float('inf')
        if self.is_empty():
            return
        for person in self.persons:
            if person.height < min_height:
                min_height = person.height
                # name = person.name
                shortest_person = person
        return shortest_person
    
    def remove_shortest(self):
        shortest_person = self.shortest()
        if shortest_person:
            for idx, person in enumerate(self.persons):
                if person == shortest_person:
                    return self.persons.pop(idx)
        return


if __name__ == "__main__":
    # room = Room()
    # print("Is the room empty?", room.is_empty())
    # room.add(Person("Lea", 183))
    # room.add(Person("Kenya", 172))
    # room.add(Person("Ally", 166))
    # room.add(Person("Nina", 162))
    # room.add(Person("Dorothy", 155))
    # print("Is the room empty?", room.is_empty())
    # room.print_contents()

    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()

    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()
