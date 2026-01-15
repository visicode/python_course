# Write your solution here
from csv import *
from datetime import timedelta,datetime

def cheaters()->list:
    ret=[]

    stf="start_times.csv"
    suf="submissions.csv"

    start_times={}
    with open(stf) as my_file:
        for line in reader(my_file, delimiter=";"):
            #jarmo;09:00
            start_times[line[0]]=line[1]

    task_time={}
    with open(suf) as my_file:
        for line in reader(my_file, delimiter=";"):
            #jarmo;1;8;16:05
            #check if we have already a value
            if (line[0],line[1]) in task_time.keys():
                #print(f"Line: {line[3]}")
                #print(f"Old Value: {task_time[(line[0],line[1])]}")
                if task_time[(line[0],line[1])] > line[3]:
                    #print("Do not store!")
                    continue
            #print("I store it!")
            task_time[(line[0],line[1])]=line[3]

    user_task=[]
    for task in task_time:
        #task will be like ('luukas', '8')
        end = task_time[task]
        start = start_times[task[0]]
        user_task.append((task[0],task[1],start,end)) #user,task,start,end
        if (datetime.strptime(end,"%H:%M"))-(datetime.strptime(start,"%H:%M")) > timedelta(hours=3):
            if task[0] not in ret:
                ret.append(task[0])

    return ret

