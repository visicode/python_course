# Write your solution here
from random import sample,randint,shuffle
from string import *

def generate_strong_password(amount: int,bn: bool, bs: bool)-> str:
    res=[]
    ret_str=""
    rn=0
    rs=0

    pool_letter=ascii_lowercase
    pool_special="!?=+-()#"
    pool_nums=digits

    #amount of random nums to be generated
    if bn:
        rn = randint(1,amount//3)

    #amount of random specials to be generated
    if bs:
        rs = randint(1,amount//3)

    #amount of letters
    rc = amount-(rn+rs)

    for i in range(rc):
        c = sample(pool_letter,1)
        res.append(c)

    if bn:
        for i in range(rn):
            c = sample(pool_nums,1)
            res.append(c)

    if bs:
        for i in range(rs):
            c = sample(pool_special,1)
            res.append(c)

    shuffle(res)
    for i in range(amount):
        #Why on earth does the str(res[i]) looks like ['a'] - including the [] and '' ??????
        ret_str += str(res[i])[2]

    return ret_str

if __name__ == '__main__':
    for j in range(10):
        print(generate_strong_password(8, True, True))