# Write your solution here
def invert(d: dict) -> None:
    l={}
    for key,value in d.items():
        l[value]=key
    for key,value in l.items():
        del(d[value])
        d[key]=value
    


if __name__ == '__main__':
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s)