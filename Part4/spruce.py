# Write your solution here
def spruce(num):
    print("a spruce!")
    i=1
    txt=''
    while i<=num:
        txt=(((num-i)*' ')+((i-1)*2+1)*'*')
        print(txt)
        i+=1
    print(((num-1)*' ')+'*')
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)