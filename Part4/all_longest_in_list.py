# Write your solution here
def all_the_longest (ls: list) -> list:
    result = []
    result.append("")
    for szo in ls:
        if len(szo)>len(result[0]):
            result.clear()
            result.append(szo)
        elif len(szo)==len(result[0]):
            result.append(szo)
    return result


if __name__ == "__main__":
    my_list = ['Seraenina', 'Gandalf', 'Harry', 'Walter']

    result = all_the_longest(my_list)
    print(result) # ['eleventh']