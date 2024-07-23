# Write your solution here
def histogram(s: str) -> None:
    for k, v in  { i: '*'* s.count(i) for i in s}.items():
        print(f'{k} {v}')

if __name__ == '__main__':
    histogram('statistically')