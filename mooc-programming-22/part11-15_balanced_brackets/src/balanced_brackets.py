import re
def balanced_brackets(my_string: str):
    my_string = re.sub(r'[^\(\)\[\]]', '', my_string)
    # print(my_string)
    # print(len(my_string))
    if len(my_string) == 0:
        return True

    if (not (my_string[0] == '(' and my_string[-1] == ')') and 
    not (my_string[0] == '[' and my_string[-1] == ']') and
    not (my_string[0] == '{' and my_string[-1] == '}')):
        return False

    # remove first and last character
    return balanced_brackets(my_string[1:-1])