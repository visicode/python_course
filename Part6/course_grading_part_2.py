# write your solution here
def grade_me(ec: list, ex: list)-> int:
    grade=0
    ex_point=sum(ex)
    ec_points=sum(ec)//4

    if (ex_point+ec_points<15):
        grade=0
    elif (15 <= (ex_point+ec_points) <= 17):
        grade=1
    elif (18 <= (ex_point+ec_points) <= 20):
        grade=2
    elif (21 <= (ex_point+ec_points) <= 23):
        grade=3
    elif (24 <= (ex_point+ec_points) <= 27):
        grade=4
    elif (28 <= (ex_point+ec_points)):
        grade=5
#    else:
#        print("ERROR TOO BIG NUMBER!")
    return grade


if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exams_data = input("Exam points: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exams_data = "exam_points1.csv"

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

exams = {}

with open(exams_data) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "id":
            continue
        ls=[]
        for i in parts[1:]:
            ls.append(int(i))
        exams[parts[0]] = ls


for id, name in names.items():
    ec=[]
    ex=[]
    if id in exams:
        ex = exams[id]
        if id in exercises:
            ec = exercises[id]
        #only grade if there was an exam
        print(f"{name} {grade_me(ec,ex)}")
    else:
        print(f"{name} 0")
