# Write your solution here
# You can test your function by calling it within the following block
def line(n, pat):
    if pat == '':
        print('*' * n)
    else:
        print(pat[0] * n)
if __name__ == "__main__":
    line(5, "")