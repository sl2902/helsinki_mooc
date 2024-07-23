# Write your solution here
def who_won(game_board: list) -> int:
    counts = {
    1: 0,
    2: 0}
    for ele in game_board:
        # counts[0] += ele.count(0)
        counts[1] += ele.count(1)
        counts[2]+= ele.count(2)
    if counts[1] == counts[2]:
        return 0
    if counts[1] > counts[2]:
        return 1
    return 2

if __name__ == "__main__":
    print(who_won([[1, 2, 2, 2], [0, 0, 0, 1], [0, 0, 2, 1]]))