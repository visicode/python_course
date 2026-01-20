# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict)->dict:
    res={}

    lowest=999
    my_list=(person1,person2,person3)
    for i in my_list:
        if i["result1"]+i["result2"]+i["result3"]<lowest:
            lowest=i["result1"]+i["result2"]+i["result3"]
            res=i

    return res

if __name__ == '__main__':
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))

#{'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}