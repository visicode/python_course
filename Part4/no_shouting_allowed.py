# Write your solution here
def no_shouting(ls: list) -> list:
    result=[]
    for szo in ls:
        if not(szo.isupper()):
            result.append(szo)
    return result

if __name__ == '__main__':
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)