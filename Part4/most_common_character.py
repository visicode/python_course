# Write your solution here
def most_common_character (txt :str) -> str:
    mx=0
    result=""
    for i in txt:
        if txt.count(i)>mx:
            mx=txt.count(i)
            result=i
    return result


if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))