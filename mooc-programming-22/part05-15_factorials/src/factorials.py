# Write your solution here
def factorials(n: int) -> dict:
    def fact(n: int) -> int:
        f = 1
        for i in range(1, n+1):
            f *= i
        return f
    return { i: fact(i) for i in range(1, n+1)}

if __name__ == "__main__":
    print(factorials(5))