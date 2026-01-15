# Write your solution here
from random import sample

def words(n: int, beginning: str)->list:
    ret=[]

    #read file
    words=[]
    with open("words.txt") as new_file:
        for word in new_file:
            words.append(word.strip())

    #search matching words
    res=[]
    for wo in words:
        if wo.startswith(beginning.strip().lower()):
            res.append(wo)

    if len(res)<n:
        raise ValueError(f"Not enough words starts with {beginning}")
    
    ret=sample(res,n)

    return ret

if __name__ == '__main__':
    word_list = words(3, "ca")
    for word in word_list:
        print(word)