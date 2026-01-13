# Write your solution here
fn="diary.txt"

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    inp = input("Function: ")
    if inp == "0":
        print("Bye now!")
        break
    elif inp=="1":
        de = input("Diary entry: ")
        if de !="":
            with open(fn,"a") as diary:
                diary.write(f"{de}\n")
            print("Diary saved")
    elif inp=="2":
        print("Entries:")
        with open(fn) as diary:
            for line in diary:
                print(f"{line.strip()}")
