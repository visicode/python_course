# Write your solution here
def factorials(a: int)->dict:
    result={}
    if a>0:
        for i in range(a):
            l=1
            for j in range(i+1):
                l*=(j+1)
            result[i+1]=l
    return result

if __name__ == '__main__':
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])