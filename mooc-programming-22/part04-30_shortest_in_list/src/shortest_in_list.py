# Write your solution here
def shortest(lst):
    lst_num = [len(a) for a in lst]
    min_val = float('inf')
    min_idx = 0
    for i, a in enumerate(lst_num):
        if a <= min_val:
            min_val = a
            min_idx = i
    return (lst[min_idx])  


if __name__ == '__main__':
    print(shortest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))
