# Write your solution here
def no_vowels(s):
    for v in 'aeiou':
        s = s.replace(v, '')
    return s

if __name__ == '__main__':
    print(no_vowels('this is an example'))