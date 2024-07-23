# Write your solution here
def all_the_longest(lst):
    lst_num = [len(a) for a in lst]
    max_val = float('-inf')
    max_idx = 0
    for i, a in enumerate(lst_num):
        if a >= max_val:
            max_val = a
            max_idx = i

    max_lst = []
    return [lst[i] for i, a in enumerate(lst_num) if len(lst[max_idx]) == a]

if __name__ == '__main__':
    print(all_the_longest(['asas', 'erteetete', 'weerweert']))