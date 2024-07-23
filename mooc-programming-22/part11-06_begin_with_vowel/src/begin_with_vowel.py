# WRITE YOUR SOLUTION HERE:
def begin_with_vowel(words: list) -> list:
    return [c for c in words if c[0].lower() in 'aeiou']
