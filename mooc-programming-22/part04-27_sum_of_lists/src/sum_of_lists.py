# Write your solution here
def list_sum(lst1, lst2):
    return [lst1[i] + lst2[i] for i in range(len(lst1))]

if __name__ == '__main__':
    print(list_sum([1, 2, 3], [4, 5, 6]))