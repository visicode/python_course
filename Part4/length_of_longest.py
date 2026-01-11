# Write your solution here
def length_of_longest (ls :list) -> int:
    result = 0
    for szo in ls:
        if len(szo)>result:
            result=len(szo)
    return result


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)