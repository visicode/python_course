# Write your solution here
from csv import *
from datetime import timedelta,datetime

def final_points()->dict:
    ret={}

    stf="start_times.csv"
    suf="submissions.csv"

    start_times={}
    with open(stf) as my_file:
        for line in reader(my_file, delimiter=";"):
            #jarmo;09:00
            start_times[line[0]]=line[1]

    task_point={}
    with open(suf) as my_file:
        for line in reader(my_file, delimiter=";"):
            #0    ;1;2;3
            #jarmo;1;8;16:05

            #check if ending over 3 hours
            end=line[3]
            start=start_times[line[0]]
            if (datetime.strptime(end,"%H:%M"))-(datetime.strptime(start,"%H:%M")) > timedelta(hours=3):
                #print("Handed in late!")
                continue
            
            #Check if it was a lower point exists
            if (line[0],line[1]) in task_point.keys():
                if task_point[(line[0],line[1])] > line[2]:
                    #print("**Do not store!")
                    continue
            #print("**I store it!")
            task_point[(line[0],line[1])]=line[2]
    #print(task_point)

    for task in task_point:
        #task will be like ('luukas', '8')
        point = task_point[task]
        user = task[0]
        if user not in ret.keys():
            ret[user]=int(point)
        else:
            ret[user]+=int(point)

    return ret


if __name__ == '__main__':
    print(final_points())
