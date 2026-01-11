# Write your solution here
def line(num,txt):
    if (txt!="") and (num>0):
        print(txt[0]*num)
    elif (txt=="") and (num>0):
        print('*'*num)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")