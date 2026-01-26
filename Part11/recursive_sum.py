# WRITE YOUR SOLUTION HERE:

def recursive_sum(n: int)->int:
    if n<=1:
        return 1
    else:
        return n+recursive_sum(n-1)


