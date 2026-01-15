# Write your solution here
from fractions import Fraction

def fractionate(iv: int)->list:
    res=[]
    for i in range(iv):
        res.append(Fraction(1, iv))
    return res

if __name__ == '__main__':
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))