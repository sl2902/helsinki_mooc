# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    start, end = row_no, row_no + 3
    col_start, col_end = column_no, column_no + 3
    return (
        len(set([i for i in range(start, end) for i in sudoku[i][col_start: col_end] if i!= 0])) == 
        len([i for i in range(start, end) for i in sudoku[i][col_start: col_end] if i!= 0])
    )

if __name__ == "__main__":
    print(block_correct([[]], 0, 0))