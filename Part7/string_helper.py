# Write your solution here
from string import ascii_letters,digits,ascii_uppercase
def change_case(mys: str)->str:
    ret=""

    for c in mys:
        if c.lower()==c:
            ret+=c.capitalize()
        else:
            ret+=c.lower()

    return ret

def split_in_half(mys: str)->tuple:
    ret=("","")
    l=len(mys)//2
    ret=(mys[:l],mys[l:])
    return ret

def remove_special_characters(mys: str)->str:
    ret=""

    valid=ascii_letters+digits+" "
    for c in mys:
        if c in valid:
            ret+=c

    return ret

if __name__ == '__main__':
    my_string = "Well hello there!"

    print(change_case(my_string))

    p1, p2 = split_in_half(my_string)

    print(p1)
    print(p2)

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)