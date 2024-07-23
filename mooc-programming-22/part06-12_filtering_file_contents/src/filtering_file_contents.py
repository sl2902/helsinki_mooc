# Write your solution here
def filter_solutions() -> None:
    with open('solutions.csv') as f:
        w1 = open('correct.csv', 'w')
        w2 = open('incorrect.csv', 'w')
        for line in f:
            line_split = line.strip().split(';')
            a, r = line_split[1], line_split[-1]
            print(a, r)
            if eval(a) == int(r):
                w1.write(line)
            else:
                w2.write(line)
    w1.close(); w2.close()

if __name__ == "__main__":
    filter_solutions()
