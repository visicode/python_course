# Write your solution here
def times_ten (a :int, b: int)->dict:
    result={}
    for i in range(a,b+1):
        result[i]=i*10
    return result
    


if __name__ == '__main__':
    d = times_ten(3, 6)
    print(d)