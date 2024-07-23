# write your solution here
def largest() -> int:
    max_val = float('-inf')
    filename = 'numbers.txt'
    with open(filename, 'r') as f:
        for line in f:
            if int(line.strip()) > max_val:
                max_val = int(line.strip())
    return max_val

if __name__ == "__main__":
    print(largest())