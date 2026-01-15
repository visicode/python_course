# Write your solution here
from datetime import *

fn = input("Filename: ")
sds = input("Starting date: ")
ma = datetime.strptime(sds, "%d.%m.%Y")
kd = ma
dai = int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")

data_str=[]
for i in range(dai):
    imp = input(f"Screen time {ma.strftime("%d.%m.%Y")}: ")
    data_str.append(imp)
    ma=ma+timedelta(1)
ma=ma-timedelta(1) #compensation of last incrementmam

data=[]
total=0
for line in data_str:
    fp,mp = line.strip().split(" ",1)
    sp,tp = mp.split(" ",1)
    data.append((int(fp),int(sp),int(tp)))
    total += int(fp)+int(sp)+int(tp)


with open(fn,"w") as filesave:
    filesave.write(f"Time period: {kd.strftime("%d.%m.%Y")}-{ma.strftime("%d.%m.%Y")}\n")
    filesave.write(f"Total minutes: {total}\n")
    filesave.write(f"Average minutes: {total/dai:.1f}\n")
    ma = kd
    for i in range(dai):
        filesave.write(f"{ma.strftime("%d.%m.%Y")}: {data[i][0]}/{data[i][1]}/{data[i][2]}\n")
        ma=ma+timedelta(1)

print(f"Data stored in file {fn}")

