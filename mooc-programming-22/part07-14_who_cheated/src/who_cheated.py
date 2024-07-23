# Write your solution here
import datetime
import re
def cheaters() -> list:
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
    
    end_times = []
    cheats = {}
    for i, name in enumerate(sub_names):
        start_time = students.get(name)
        # st_hr, st_mins = int(start_time.split(':')[0]), int(start_time.split(':')[1]) 
        # end_hr, end_mins = int(sub_rest[i][2].split(':')[0]), int(sub_rest[i][2].split(':')[1]) 
        # start_time = datetime.timedelta(hours=st_hr, minutes=st_mins)
        # end_time = datetime.timedelta(hours=end_hr, minutes=end_mins)
        start_time = datetime.datetime.strptime(start_time, '%H:%M')
        end_time = datetime.datetime.strptime(sub_rest[i][2], '%H:%M')
        diff = (end_time - start_time).seconds / 3600
        if not name in cheats:
            cheats[name] = [diff]
        else:
            cheats[name].append(diff)
    
    return [k for k, v in cheats.items() if max(v) > 3]

if __name__ == "__main__":
    print(cheaters())
