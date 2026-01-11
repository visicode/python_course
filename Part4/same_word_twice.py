# Write your solution here
my_list=[]
while True:
    txt = input("Word")
    if txt in my_list:
        print("You typed in",len(my_list),"different words")
        break
    else:
        my_list.append(txt)
