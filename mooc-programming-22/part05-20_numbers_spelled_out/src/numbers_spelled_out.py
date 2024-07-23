# Write your solution here
def dict_of_numbers() -> dict:
    numbers = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
    }
    for n in range(21, 100):
        if n not in numbers:
            numbers[n] = numbers[(n//10)*10].lower() + '-' + numbers[n%10].lower()
    return numbers

if __name__ == "__main__":
    numbers = dict_of_numbers()
    print(numbers[20])
    print(numbers[23])
    print(numbers[45])
    print(numbers[59])
    print(numbers[99])