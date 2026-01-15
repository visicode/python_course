# Write your solution here
from random import choice
def roll(dice: str)->str:
    ret=""
    a=[3, 3, 3, 3, 3, 6]
    b=[2, 2, 2, 5, 5, 5]
    c=[1, 4, 4, 4, 4, 4]

    if dice=="A":
        ret=choice(a)
    elif dice=="B":
        ret=choice(b)
    else:
        ret=choice(c)
    

    return ret

def play(die1: str, die2: str, times: int)->tuple:
    res1=0
    res2=0
    w1=0
    w2=0
    eq=0
    for i in range(times):
        res1 = roll(die1)
        res2 = roll(die2)
        if res1>res2:
            w1+=1
        elif res1==res2:
            eq+=1
        else:
            w2+=1

    return (w1,w2,eq)

if __name__ == '__main__':
    result = play("A", "C", 1000)
    print(result)
    result = play("B", "B", 1000)
    print(result)