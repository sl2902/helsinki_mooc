# Write your solution here
# You can test your function by calling it within the following block
def spruce(n):
    i = 1
    print('a spruce!'.center(2*(n+3), ' '))
    for j in range(1, n+1):
        print(('*' * i).center(2 * (n), ' '))
        i = 2 * j + 1
    print('*'.center(2 * (n), ' '))
if __name__ == "__main__":
    spruce(3)