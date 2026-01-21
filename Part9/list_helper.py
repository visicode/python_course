# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list): #returns the most common item on the list
        fr={}
        for num in my_list:
            if num not in fr:
                fr[num]=1
            else:
                fr[num]+=1
        mx=max(fr.values())
        for key, val in fr.items():
            if val == mx:
                return(key)  
            

    @classmethod
    def doubles(cls, my_list: list): #returns the number of unique items which appear at least twice on the list
        fr={}
        for num in my_list:
            if num not in fr:
                fr[num]=1
            else:
                fr[num]+=1

        x=0
        for i in sorted(fr.values()):
            if i>=2: #at this point starts the double or more
                x=sorted(fr.values()).index(i)
                break
        return len(fr)-x
