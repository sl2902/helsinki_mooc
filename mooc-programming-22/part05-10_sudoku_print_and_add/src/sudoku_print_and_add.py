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
if __name__ == '__main__':

   
    print_sudoku(sudoku)
    # add_number(sudoku, 0, 0, 2)
    # add_number(sudoku, 1, 2, 7)
    # add_number(sudoku, 5, 7, 3)
    # print()
    # print("Three numbers added:")
    # print()
    # print_sudoku(sudoku)
