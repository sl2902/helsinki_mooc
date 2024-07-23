# Write your solution here
def column_correct(sudoku: list, column_no: int) -> bool:
        return len(set(e for e in [c[column_no] for c in sudoku] if e != 0)) == len([e for e in [c[column_no] for c in sudoku] if e != 0])

if __name__ == "__main__":
    print(column_correct([[]], 0))