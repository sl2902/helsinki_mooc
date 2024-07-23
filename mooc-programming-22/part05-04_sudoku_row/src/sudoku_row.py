# Write your solution here
def row_correct(sudoku: list, row_no: int) -> bool:
        return len(set(i for i in sudoku[row_no] if i != 0)) == len([i for i in sudoku[row_no] if i != 0])

if __name__ == "__main__":
    print(row_correct([[]], 0))