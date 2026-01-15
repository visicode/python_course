# Write your solution here
from random import sample
from string import *

def generate_password(amount: int)-> str:
    res=""

    pool=ascii_lowercase
    for i in range(amount):
        c = sample(pool,1)
        res+=c[0]

    return res

if __name__ == '__main__':
    for i in range(10):
        print(generate_password(8))