# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict) -> dict:
    person_list = [person1, person2, person3]
    avg = []
    for person in person_list:
        sum, c = 0, 0
        for k in person:
            if isinstance(person[k], int):
                sum += person[k]
                c += 1
        
        avg.append(sum/c)
    return person_list[avg.index(min(avg))]

if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}
    print(smallest_average(person1, person2, person3))
