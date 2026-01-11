# Write your solution here
def no_vowels(txt :str) -> str:
    result=""
    for c in txt:
        if c not in ['a','i','e','o','u']:
            result+=c
    return result

if __name__ == '__main__':
    my_string = "this is an example"
    print(no_vowels(my_string))