# Copy here code of line function from previous exercise
def line(num,txt):
    if (txt!="") and (num>0):
        print(txt[0]*num)
    elif (txt=="") and (num>0):
        print('*'*num)

def square_of_hashes(size):
    lines=size    
    while lines > 0:
        line(size, "#")
        lines -= 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
