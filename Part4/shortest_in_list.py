# Write your solution here
def shortest(ls :list) -> str:
    result=ls[0]
    for szo in ls:
        if len(szo)<len(result):
            result=szo
    return result


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)