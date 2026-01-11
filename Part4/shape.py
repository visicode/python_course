# Copy here code of line function from previous exercise and use it in your solution
def line(num,txt):
    if (txt!="") and (num>0):
        print(txt[0]*num)
    elif (txt=="") and (num>0):
        print('*'*num)

def triangle(size,car):
    i=1
    while i<=size:
        line(i, car)
        i+=1

def box(width,height,car):
    while height > 0:
        line(width, car)
        height -= 1

def shape(n1,c1,n2,c2):
    triangle(n1,c1)
    box(n1,n2,c2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")