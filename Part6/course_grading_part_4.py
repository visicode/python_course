# tee ratkaisu tänne
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
    return grade


if True:
    # this is never executed
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exams_data = input("Exam points: ")
    course_data = input("Course information: ")
else:
    # hard-coded input
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exams_data = "exam_points1.csv"
    course_data = "course1.txt"

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

course = []
name=""
credit=0
with open(course_data) as new_file:
    for line in new_file:
        if "name:" in line.strip():
            name=line.strip().split(":")[1].strip()
            course.append(name)
        if "credits:" in line.strip():
            credit=int(line.strip().split(":")[1])
            course.append(credit)

rest="results.txt"
with open(rest,"w") as new_file:
    head = f"{course[0]}, {course[1]} credits"
    new_file.write(f"{head}\n")
    head2="="*len(head)
    new_file.write(f"{head2}\n")
    new_file.write(f"name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")

    for id, name in names.items():
        ec=[]
        ex=[]
        if id in exams:
            ex = exams[id]
            if id in exercises:
                ec = exercises[id]
                p1 = sum(ec)
                p2 = p1//4
                p3 = sum(ex)
                p4 = p2+p3
                #only grade if there was an exam
                new_file.write(f"{name:30}{p1:<10}{p2:<10}{p3:<10}{p4:<10}{grade_me(ec,ex):<10}\n")

resc="results.csv"
with open(resc,"w") as new_file:
    for id, name in names.items():
        ec=[]
        ex=[]
        if id in exams:
            ex = exams[id]
            if id in exercises:
                ec = exercises[id]
                new_file.write(f"{id};{name};{grade_me(ec,ex)}\n")

print("Results written to files results.txt and results.csv")