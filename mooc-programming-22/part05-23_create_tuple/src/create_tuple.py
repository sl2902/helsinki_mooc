# Write your solution here
def create_tuple(x: int, y: int, z: int) -> tuple:
    f = min(x, y, z)
    l = max(x, y, z)
    t = x + y + z
    return (f, l, t)

if __name__ == "__main__":
    print(create_tuple(5, 3, -1))