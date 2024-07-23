# Write your solution here
import datetime
from collections import defaultdict
def final_points() -> list:
    students = {}
    with open('start_times.csv', 'r') as f:
        for line in f:
            line = line.strip().split(';')
            if not line[0] in students:
                students[line[0]] = line[1]
    sub_names, sub_rest =[], []
    with open('submissions.csv', 'r') as f:
        for line in f:
            line = line.strip().split(';')
            sub_names.append(line[0])
            sub_rest.append(line[1:])

    final = defaultdict(lambda: defaultdict(list))
    for i, name in enumerate(sub_names):
            start_time = students.get(name)
            start_time = datetime.datetime.strptime(start_time, '%H:%M')
            end_time = datetime.datetime.strptime(sub_rest[i][2], '%H:%M')
            diff = (end_time - start_time).seconds / 3600
            # if name == 'kjell':
            #     print(sub_rest[i][0], diff, sub_rest[i][1])
            if diff  <= 3:
                final[name][sub_rest[i][0]].append(sub_rest[i][1])
    # print(final['kjell'])
    
    cheaters = {}
    for d_ in final:
        ind_points = 0
        for k, v in final[d_].items():
            ind_points += max(int(i) for i in v)
        cheaters[d_] = ind_points


    return cheaters

if __name__ == "__main__":
    print(final_points())