# Write your solution here
exams=[]
exers=[]
i=0
while True:
    txt = input("Exam points and exercises completed: ")
    if txt=="":
        break
    ml = txt.split()
    exams.append(int(ml[0]))
    exers.append(int(ml[1])//10)
    i+=1
print("Statistics:")

ave = (sum(exams)+sum(exers))/len(exams)
print(f"Points average: {ave:.1f}")

pas = 0
for i in range(len(exams)):
    if (exams[i]>=10) and (exams[i]+exers[i]>=15):
        pas +=1
pps = 100*(pas/len(exams))
print(f"Pass percentage: {pps:.1f}")

print("Grade distribution: ")
grades=[]
for i in range(len(exams)):
    if (exams[i]<10) or (exams[i]+exers[i]<15):
        grades.append(0)
    elif (15 <= (exams[i]+exers[i]) <= 17):
        grades.append(1)
    elif (18 <= (exams[i]+exers[i]) <= 20):
        grades.append(2)
    elif (21 <= (exams[i]+exers[i]) <= 23):
        grades.append(3)
    elif (24 <= (exams[i]+exers[i]) <= 27):
        grades.append(4)
    elif (28 <= (exams[i]+exers[i]) <= 30):
        grades.append(5)                        
    else:
        print("ERROR TOO BIG NUMBER!")

for i in range(5,-1,-1):
    print(f"{i}: "+(grades.count(i))*'*')
