# Write your solution here
def change_case(my_string: str) -> str:
    new_string = ''
    for c in my_string:
        if c.isupper():
            new_string += c.lower()
        elif c.islower():
            new_string += c.upper()
        else:
            new_string += c
    return new_string

def split_in_half(orig_string: str) -> tuple:
    return orig_string[:len(orig_string)//2], orig_string[len(orig_string)//2:]

def remove_special_characters(orig_string: str) -> str:
    return ''.join(c for c in orig_string if c.isalnum() or c == ' ')

if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)
