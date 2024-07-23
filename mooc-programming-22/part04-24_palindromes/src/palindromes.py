# Write your solution here
def palindromes(str1):
    return str1 == str1[::-1]

def main():
    while 1:
        s = input('Please type in a palindrome: ')
        if  palindromes(s):
           print(f'{s} is a palindrome!')
           break
        else:
            print("that wasn't a palindrome")
main()
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
