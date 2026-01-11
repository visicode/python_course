# Write your solution here
my_list=[]
while True:
    val = int(input("New item: "))
    if val != 0:
        my_list.append(val)
        print("The list now:",my_list)
        print("The list in order:",sorted(my_list))
    else:
        break
print("Bye!")