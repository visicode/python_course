# Write your solution here
dick={}
while True:
    com = input("command (1 search, 2 add, 3 quit): ")
    if com=="2":
        key = input("name: ")
        value = input("number: ")
        if key not in dick:
            dick[key]=[]
        dick[key].append(value)
        print("ok!")
    elif com=="1":
        key = input("name: ")
        if key in dick:
            for num in dick[key]:
                print(num)
        else:
            print("no number")
    else:
        print("quitting...")
        break
