# Write your solution here
def transpose(mx: list):
    temp = 0
    dim = len(mx[0])
    for i in range(dim):
        for j in range(i,dim):
            temp=mx[i][j]
            mx[i][j]=mx[j][i]
            mx[j][i]=temp
