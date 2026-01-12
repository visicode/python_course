# Write your solution here
def double_items (ls: list) -> list:
    nls = []
    for i in ls:
        nls.append(i*2)
    return nls

if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)