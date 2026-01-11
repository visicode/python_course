# Write your solution here
def distinct_numbers (ls :list) -> list:
    result = []
    helper = sorted(ls)
    for i in range(len(helper)):
        if helper[i] not in result:
            result.append(helper[i])
    return result


if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]