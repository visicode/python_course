# Write your solution here
def longest (ls: list) -> str:
    result=""
    for txt in ls:
        if len(txt)>len(result):
            result = txt
    return result

if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))
