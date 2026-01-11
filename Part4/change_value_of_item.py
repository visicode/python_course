# Write your solution here
my_list=[1,2,3,4,5]
while True:
    ndx = int(input("Index: "))
    if ndx==-1:
        break
    val = int(input("New value: "))
    my_list[ndx]=val
    print(my_list)

