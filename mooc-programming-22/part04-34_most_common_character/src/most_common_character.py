# Write your solution here
def most_common_character(s):
    s_count = [s.count(c) for c in s]
    max_val = float('-inf')
    max_id = 0
    for i, v in enumerate(s_count):
        if v > max_val:
            max_val = v
            max_id = i
    return s[max_id]

if __name__ == '__main__':
    print(most_common_character('exemplaryelementary'))