# Write your solution here
def check_nums(lottery_num: list) -> bool:
    if len(lottery_num) != 7:
        return False
    for n in lottery_num:
        if not n.isdigit():
            return False
        if not (1<= int(n) <= 39):
            return False
        if lottery_num.count(n) > 1:
            return False
    return True

def filter_incorrect() -> None:
    with open('lottery_numbers.csv', 'r') as f, open('correct_numbers.csv', 'w') as w:
        for line in f:
            mod_line = line.strip().split(';')
            wk, nums = mod_line[0], mod_line[1:][0].split(',')
            _, wk_num = wk.split()
            if wk_num.isdigit() and check_nums(nums):
                w.write(line)
# filter_incorrect()
            

