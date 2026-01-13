# write your solution here

def read_fruits()-> dict:
    res={}
    with open("fruits.csv") as new_file:
        for line in new_file:
            line = line.replace("\n", "")
            parts = line.split(";")
            name = parts[0]
            price = float(parts[1])
            res[name]=price
        #print (res)
        return res
    
if __name__ == '__main__':
    read_fruits()