# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(n, pat):
    if pat == '':
        print('*' * n)
    else:
        print(pat[0] * n)

def rect(size1, size2, character):
    # You should call function line here with proper parameters
    for _ in range(size2):
        line(size1, character)

def triangle(size, character):
    # You should call function line here with proper parameters
    for i in range(1, size+1):
        line(i, character)

def shape(size1, char1, size2, char2):
    triangle(size1, char1)
    rect(size1, size2, char2)

if __name__ == "__main__":
    shape(5, "x", 2, "o")