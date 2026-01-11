# Write your solution here
def even_numbers (ls :list) -> list:
    result = []
    for i in ls:
        if i%2==0:
            result.append(i)
    return result


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    new_list = even_numbers(my_list)
    print("original", my_list)
    print("new", new_list)