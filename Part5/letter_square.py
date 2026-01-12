# Write your solution here
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = int(input("Layers: "))
res=[]
for i in range(num):
    temp=[]
    if res==[]:
        res.append(ABC[i])
    else:
        l=len(res)
        temp.append(ABC[i]*(l+2))
        for j in range(l):
            temp.append(ABC[i]+res[j]+ABC[i])
        temp.append(ABC[i]*(l+2))
        res=temp.copy()

for j in range(2*num-1):
    print(res[j])

