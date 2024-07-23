# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    start, end = row_no, row_no + 3
    col_start, col_end = column_no, column_no + 3
    return (
        len(set([i for i in range(start, end) for i in sudoku[i][col_start: col_end] if i!= 0])) == 
        len([i for i in range(start, end) for i in sudoku[i][col_start: col_end] if i!= 0])
    )

def column_correct(sudoku: list, column_no: int) -> bool:
        return (
            len(set(e for e in [c[column_no] for c in sudoku] if e != 0)) == 
            len([e for e in [c[column_no] for c in sudoku] if e != 0])
        )

def row_correct(sudoku: list, row_no: int) -> bool:
        return (
            len(set(i for i in sudoku[row_no] if i != 0)) == 
            len([i for i in sudoku[row_no] if i != 0])
        )

def sudoku_grid_correct(sudoku: list) -> bool:
    for r in range(9):
        if not row_correct(sudoku, r):
            return False
        for c in range(9):
             if not column_correct(sudoku, c):
                return False
             if (r, c) not in [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]: 
                continue
             if not block_correct(sudoku, r, c):
                return False
            
    return True

if __name__ == "__main__":
    print(sudoku_grid_correct([[]]))

