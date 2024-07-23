# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        max_item = max([my_list.count(item) for item in set(my_list)])

        for item in set(my_list):
            if my_list.count(item) == max_item:
                return item

    @classmethod
    def doubles(cls, my_list: list):
        return sum([1 for i in set(my_list) if my_list.count(i) >= 2])

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
