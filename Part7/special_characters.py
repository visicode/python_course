# Write your solution here
from string import *
def separate_characters(ms: str)->tuple:
    res=["","",""]
    for c in ms:
        if c in ascii_letters:
            res[0]+=c
        elif c in punctuation:
            res[1]+=c
        else:
            res[2]+=c
    return (res[0],res[1],res[2])

if __name__ == '__main__':
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])