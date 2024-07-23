# write your solution here
def row_sums() -> list:
    ros_agg = []
    filename = 'matrix.txt'
    with open(filename, 'r') as f:
       row_agg = [sum([int(n) for n in line.strip().split(',')]) for line in f ]
    return row_agg

def row_max() -> list:
    ros_agg = []
    filename = 'matrix.txt'
    with open(filename, 'r') as f:
       row_agg = [max([int(n) for n in line.strip().split(',')]) for line in f ]
    return row_agg

def matrix_sum() -> int:
    mat_sum = 0
    for r in row_sums():
        mat_sum += r
    return mat_sum

def matrix_max() -> int:
    return max(row_max())

if __name__ == "__main__":
    print(matrix_sum())



