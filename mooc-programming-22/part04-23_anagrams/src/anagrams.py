# Write your solution here
def anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

if __name__ == "__main__":
    print(anagrams('bun', 'sun'))