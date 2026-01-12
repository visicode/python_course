# Write your solution here
dick={}
while True:
    com = input("command (1 search, 2 add, 3 quit): ")
    if com=="2":
        key = input("name: ")
        value = input("number: ")
        dick[key]=value
        print("ok!")
    elif com=="1":
        key = input("name: ")
        if key in dick:
            print(dick[key])
        else:
            print("no number")
    else:
        print("quitting...")
        break
