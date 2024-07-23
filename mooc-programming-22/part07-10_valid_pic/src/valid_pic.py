# Write your solution here
import datetime
def is_it_valid(pic: str) -> bool:
    if len(pic) != 11:
        return False
    if not pic[:6].isdigit():
        return False
    if not pic[6] in ['+', '-', 'A']:
        return False
    try:
        if pic[6] == 'A':
            year = int('20' + pic[4:6])
        elif pic[6] == '+':
            year = int('19' + pic[4:6])
        else:
            year = int('18' + pic[4:6])
        datetime.datetime(year, int(pic[2:4]), int(pic[:2]))
    except:
        return False
    if not '0123456789ABCDEFHJKLMNPRSTUVWXY'[int(pic[:6] + pic[7:10]) % 31] == pic[-1]:
        return False
    return True

# print(is_it_valid('100400A644E'))