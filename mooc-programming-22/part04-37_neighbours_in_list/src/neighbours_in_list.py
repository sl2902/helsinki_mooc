# Write your solution here
def longest_series_of_neighbours(lst):
    a0 = lst[0]
    is_longest = False
    c = 1
    c_lst  = []
    for v in lst[1:]:
        if abs(v - a0) == 1:
            c+= 1
        else:
            # if c!= 1:
            c_lst.append(c)
            c = 1
        a0 = v
    # if c!= 1:
    c_lst.append(c)
    return(max(c_lst))

if __name__ == '__main__':
    print(longest_series_of_neighbours([1, 5]))