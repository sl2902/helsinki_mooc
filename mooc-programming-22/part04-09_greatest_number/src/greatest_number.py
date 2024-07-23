# Write your solution here
# You can test your function by calling it within the following block
def greatest_number(a, b, c):
    if a > b:
        if b > c:
            return a
        if c > a:
            return c
        return a
    if b > c:
        return b
    return c
if __name__ == "__main__":
    greatest = greatest_number(9, -1, 3)
    print(greatest)