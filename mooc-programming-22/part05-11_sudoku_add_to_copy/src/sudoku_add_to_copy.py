# Write your solution here
def print_sudoku(sudoku: list) -> None:
    for j, r in enumerate(sudoku):
        for i, c in enumerate(r):
            if c > 0:
                if i in [3, 6]:
                    print(f' {c} ', end='')
                else:
                    print(f'{c} ', end='')
            else:
                if i in [3, 6]:
                    print(' _ ', end='')
                else:
                    print('_ ', end="")
        if j in [2, 5]:
            print()
            print()
        else:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int) -> None:
    sudoku[row_no][column_no] = number
    # print(sudoku)

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> None:
    new_sudoko = [a[:] for a in sudoku]
    add_number(new_sudoko, row_no, column_no, number)
    return new_sudoko

if __name__ == '__main__':

    sudoku = sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)