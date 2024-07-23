# Write your solution here
# You can test your function by calling it within the following block
def same_chars(s, start, end):
    if start < end and end < len(s):
        return s[start] == s[end]
    return False
if __name__ == "__main__":
    print(same_chars("pp", 0, 1))