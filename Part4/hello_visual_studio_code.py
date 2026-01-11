# Write your solution here
mystring = "Visual Studio"
while True:
    mystring = input("Editor: ")
    if mystring.lower() in ["notepad","word"]:
        print("awful")
    elif mystring.lower()!="visual studio code":
        print("not good")
    else:
        print("an excellent choice!")
        break
