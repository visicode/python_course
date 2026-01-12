# Write your solution here
def remove_smallest (ls: list):
    mn = min(ls)
    ls.remove(mn)

if __name__ == "__main__":
    numbers = [2, 4, 6, 1, 3, 5]
    remove_smallest(numbers)
    print(numbers)