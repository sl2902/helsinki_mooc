# Write your solution here
def row_sums(my_matrix: list) -> None:
    for i, arr in enumerate(my_matrix):
        my_matrix[i] = arr + [sum(arr)]
        

if __name__ == "__main__":
    my_matrix = [[1, 2], [3, 4]]
    row_sums(my_matrix)
    print(my_matrix)
