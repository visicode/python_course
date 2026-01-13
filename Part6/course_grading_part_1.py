# write your solution here

if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"

names = {}

with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        names[parts[0]] = parts[1].strip()+' '+parts[2].strip()

exercises = {}

with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        ls=[]
        for i in parts[1:]:
            ls.append(int(i))
        exercises[parts[0]] = ls


for id, name in names.items():
    if id in exercises:
        ls = exercises[id]
        print(f"{name} {sum(ls)}")
    else:
        print(f"{name} 0")

#Student information: students1.csv
#Exercises completed: exercises1.csv
#pekka peloton 21
#jaana javanainen 27
#liisa virtanen 35