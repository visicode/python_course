# Write your solution here
import urllib.request
import json

def retrieve_all() -> list:
    ret=[]

    urli="https://studies.cs.helsinki.fi/stats-mock/api/courses"    
    my_request = urllib.request.urlopen(urli)
    data = my_request.read()
    courses = json.loads(data)
    
    for course in courses:
        if course["enabled"]:
            my_tup = (course["fullName"],course["name"],course["year"],sum(course["exercises"]))
            ret.append(my_tup)

    return ret

#https://studies.cs.helsinki.fi/stats-mock/api/courses/****/stats

def retrieve_course(cn: str)->dict:
    ret={}
    urli=f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{cn}/stats"    

    my_request = urllib.request.urlopen(urli)
    data = my_request.read()
    stats = json.loads(data)

    ret['weeks']=len(stats)
    ms = 0 #max students
    sh = 0 #sum hours_total
    se = 0 #sum excer_total

    #goes through the weeks number
    for wk_n in stats:
        #grab the given week data
        wk=stats[wk_n]
        
        if wk['students']>ms:
            ms=wk['students']
        sh+=wk['hour_total']
        se+=wk['exercise_total']

        

    ret['students']=ms
    ret['hours']=sh
    ret['hours_average']=sh//ms
    ret['exercises']=se
    ret['exercises_average']=se//ms

    return ret


if __name__ == '__main__':
    course="docker2019"
    print(retrieve_course(course))
