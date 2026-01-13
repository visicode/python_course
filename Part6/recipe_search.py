# Write your solution here
def search_by_name(fn: str, sw: str)-> list:
    res=[]
    ll=""
    with open(fn) as new_file:
        for word in new_file:
            #Last line was empty then Receipe comes
            if ll.strip()=="":
                if sw.lower() in word.lower():
                    res.append(word.strip())
            ll=word
            #print(word)

    return res

def search_by_time(fn: str,num: int)-> list:
    rec=[]
    res=[]
    ll=""
    act_rec=""
    found=False

    with open(fn) as new_file:
        for word in new_file:
            #Last line was empty then Receipe comes
            if ll.strip()=="":
                act_rec=word.strip()
                found=True
            #Last line was Receipe now the time comes
            elif found:
                rec.append((act_rec,int(word)))
                found=False
            ll=word

    for cur in rec:
        if cur[1]<=num:
            res.append(f"{cur[0]}, preparation time {cur[1]} min")

    return res

def search_by_ingredient(fn: str, sw: str)->list:
    rec=[]
    res=[]
    ll=""
    act_rec=""
    act_time=0
    f_rec=False

    with open(fn) as new_file:
        for word in new_file:
            #Last line was empty then Receipe comes
            if ll.strip()=="":
                act_rec=word.strip()
                f_rec=True
            #Last line was Receipe now the time comes
            elif f_rec:
                act_time=int(word)
                f_rec=False
            #Ingridient
            elif word.strip()!="":
                if word.lower().strip()==sw.lower().strip():
                    rec.append((act_rec,act_time))
            ll=word

    #print(rec)

    for cur in rec:
        res.append(f"{cur[0]}, preparation time {cur[1]} min")

    return res



if __name__ == '__main__':

    found_recipes = search_by_ingredient("recipes1.txt", "milk")

    for recipe in found_recipes:
        print(recipe)