# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
    

class Box:
    def __init__(self):
        self.boxes = []

    def add_present(self, present: Present):
        self.boxes.append(present.weight)
    
    def total_weight(self):
        return sum(self.boxes)

if __name__ == "__main__":
    book = Present("ABC Book", 2)

    box = Box()
    box.add_present(book)
    print(box.total_weight())

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
