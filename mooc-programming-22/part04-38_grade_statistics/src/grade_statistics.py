# Write your solution here
from functools import total_ordering
import math
n_sub, overall_points, pass_total = 0, 0, 0
grades = {0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0
    }
while 1:
    score = input('Exam points and exercises completed: ')
    if len(score) == 0:
        break
    
    e_p, e_c = int(score.split()[0]), int(score.split()[1])

    total_points = math.floor(e_c) // 10 + e_p
    if total_points >= 15 and e_p > 9:
        pass_total += 1

    overall_points += total_points
    n_sub += 1
  
    if e_p < 10 or total_points < 15:
        grades[0] += 1
    elif total_points < 18 and e_p > 9:
        grades[1] += 1
    elif total_points < 21 and e_p > 9:
        grades[2] += 1
    elif total_points < 24 and e_p > 9:
        grades[3] += 1
    elif total_points < 28 and e_p > 9:
        grades[4] += 1
    elif total_points <= 30 and e_p > 9:
        grades[5] += 1
print('Statistics:')
print(f'Points average: {overall_points/n_sub}')
print(f'Pass percentage: {100 * pass_total/n_sub:.1f}')
print('Grade distribution:')
print(f'{5:>3}: {grades[5] * "*"}')
print(f'{4:>3}: {grades[4] * "*"}')
print(f'{3:>3}: {grades[3] * "*"}')
print(f'{2:>3}: {grades[2] * "*"}')
print(f'{1:>3}: {grades[1] * "*"}')
print(f'{0:>3}: {grades[0] * "*"}')
