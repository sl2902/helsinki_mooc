# Write your solution here
import urllib.request
import json
def retrieve_all() -> list:
    int_result, result = [], []
    # enabled = []
    url = 'https://studies.cs.helsinki.fi/stats-mock/api/courses'
    my_request = urllib.request.urlopen(url)
    my_request = json.loads(my_request.read())
    for d_item in my_request:
       if d_item['enabled']:
        result.append((d_item['fullName'], d_item['name'], d_item['year'], sum(d_item['exercises'])))
    
    # # prepare data for custom sort
    # for courses in enabled:
    #     tmp = []
    #     for key, val in courses.items():
    #         if key == 'fullName': #['fullName', 'name', 'year', 'exercises']:
    #             tmp.append([val, 1])
    #         elif key == 'name':
    #             tmp.append([val, 2])
    #         elif key == 'year':
    #             tmp.append([val, 3])
    #         elif key == 'exercises':
    #             tmp.append([sum(val), 4])
    #     int_result.append(tmp)
    
    # for r in int_result:
    #     tmp = []
    #     for rr in (sorted(r, key=lambda x: x[-1])):
    #         tmp.append(rr[0])
    #     result.append(tuple(tmp))
        
    return result

def retrieve_course(course_name: str) -> dict:
    # base_url = 'https://studies.cs.helsinki.fi/stats-mock/api/courses/'
    course_url = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats'
    # my_request1 = urllib.request.urlopen(base_url)
    # my_request1 = json.loads(my_request1.read())
    my_request2 = urllib.request.urlopen(course_url)
    my_request2 = json.loads(my_request2.read())

    results = {}
    # for item in my_request1:
    #     if item['name'] == course_name:
    #         results['weeks'] = item['week']
    #         break
    
    results['weeks'] = len(my_request2)
    for k in my_request2:
        results['students'] = my_request2[k]['students']
        break

    results['hours'] = 0
    for d_ in my_request2:
        results['hours'] += my_request2[d_]['hour_total']
    
    results['hours_average'] = results['hours'] // results['students']

    results['exercises'] = 0
    for d_ in my_request2:
        results['exercises'] += my_request2[d_]['exercise_total']
    
    results['exercises_average'] = results['exercises'] // results['students']


    return results

if __name__ == "__main__":
    print(retrieve_all())
    print (retrieve_course("CCFUN"))

