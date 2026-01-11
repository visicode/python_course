# Write your solution here
val = int(input("How many items: "))
i=1
my_list=[]
while i<=val:
    item = int(input(f"Item {i}: "))
    my_list.append(item)
    i+=1
print(my_list)
