# write your solution here

txt = input("Write text: ")
#txt = "This is acually a good and usefull program"
lstxt = txt.split()

words=[]
with open("wordlist.txt") as new_file:
    for word in new_file:
        words.append(word.strip())

for w in lstxt:
    if w.lower() in words:
        print(f"{w} ",end="")
    else:
        print(f"*{w}* ",end="")
print()
#This is *acually* good and *usefull* program
