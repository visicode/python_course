# Write your solution here
def count_matching_elements (ls: list, num: int) -> int:
    result=0
    for row in ls:
        result+=row.count(num)
    return result

if __name__ == '__main__':
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))