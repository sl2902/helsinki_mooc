# Write your solution here
def formatted(lst):
    return [f'{n:.2f}' for n in lst]

if __name__ == '__main__':
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))