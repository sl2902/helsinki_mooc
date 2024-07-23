# Write your solution here
import json
def print_persons(filename: str) -> None:
    with open(filename, 'r') as f:
        data = json.load(f)
    for d_ in data:
        for k, v, in d_.items():
            if isinstance(v, int):
                print(f'{v} years (', end='')
            elif isinstance(v, list):
                print(*v, end='', sep=', ')
                print(')')
            else:
                print(f'{v} ', end='')
        # print()

# print_persons('file1.json')