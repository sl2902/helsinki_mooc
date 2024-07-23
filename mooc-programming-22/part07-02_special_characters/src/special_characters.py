# Write your solution here
def separate_characters(my_string: str) -> tuple:
    import string
    asc_str, punc_str, oth_str = '', '', ''
    for c in my_string:
        if c in string.ascii_letters:
            asc_str += c
        elif c in string.punctuation:
            punc_str += c
        else:
            oth_str += c
    return asc_str, punc_str, oth_str

# parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
# print(parts[0])
# print(parts[1])
# print(parts[2])