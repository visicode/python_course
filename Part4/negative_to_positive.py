# Write your solution here
num = int(input("Please type in a positive integer: "))
if num>0:
    for i in range(-num,num):
        if i<0:
            print(i)
        else:
            print(i+1)
