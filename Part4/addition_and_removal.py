# Write your solution here
my_list=[]
letter=''
val=1
while letter!='x':
    print("The list is now",my_list)
    letter = input("a(d)d, (r)emove or e(x)it: ")
    if letter== 'd':
        my_list.append(val)
        val+=1
    if letter == 'r':
        my_list.pop()
        val-=1
print("Bye!")