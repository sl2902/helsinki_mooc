# write your solution here
def read_fruits() -> dict:
    prices = {}
    with open('fruits.csv', 'r') as f:
        for line in f:
            k, v = line.strip().split(';')
            if not k in prices:
                prices[k] = float(v)
    return prices

if __name__ == "__main__":
    print(read_fruits())