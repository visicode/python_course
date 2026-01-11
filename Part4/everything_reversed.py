# Write your solution here
def everything_reversed(ls: list) -> list:
    result=[]
    lsr=ls.copy()
    lsr.reverse()
    for szo in lsr:
        result.append(szo[::-1])
    return result

if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)