# WRITE YOUR SOLUTION HERE:
class Recording:
    def __init__(self, length: int):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length should be greater 0")
    
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, length):
        if length > 0:
            self.__length = length
        else:
            raise ValueError("Length should be greater 0")

if __name__ == "__main__":
    the_wall = Recording(43)
    print(the_wall.length)
    the_wall.length = 44
    print(the_wall.length)
