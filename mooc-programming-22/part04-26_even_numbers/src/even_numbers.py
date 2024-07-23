# Write your solution here
def even_numbers(lst):
    # print('original', lst)
    return [a for a in lst if a%2 == 0]

if __name__ == '__main__':
    print(even_numbers([1, 2]))
