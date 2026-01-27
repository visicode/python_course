from math import sqrt
# Write your solution here
def prime_numbers():
    mx=2
    mls=[]
    if len(mls)==0:
        mls.append(mx)
        yield mx
        mx+=1
    while True:
        nah=False
        for j in range(len(mls)):
            if mx%mls[j]==0: #dividable with an earlier prime number
                mx+=2
                nah=True
                break
            if mls[j]>sqrt(mx) : # enough going until sqrt(mx)
                break

        if not nah:
            mls.append(mx)
            yield mx
            mx+=2 #enough check odd numbers

