# write your solution here
from difflib import get_close_matches

txt = input("Write text: ")
#txt = "This is acually a good and usefull program"
lstxt = txt.split()

words=[]
with open("wordlist.txt") as new_file:
    for word in new_file:
        words.append(word.strip())

sug=[]
for w in lstxt:
    if w.lower() in words:
        print(f"{w} ",end="")
    else:
        print(f"*{w}* ",end="")
        sug.append(w)
print("\nsuggestions:")

for w in sug:
    print(f"{w}: ",end="")
    for su in get_close_matches(w,words):
        print(f"{su}, ",end="")
    print()

