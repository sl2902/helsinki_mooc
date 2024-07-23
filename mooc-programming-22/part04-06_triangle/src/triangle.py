# Copy here code of line function from previous exercise
def line(n, pat):
    if pat == '':
        print('*' * n)
    else:
        print(pat[0] * n)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1, size+1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
