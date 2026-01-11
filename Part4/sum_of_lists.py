# Write your solution here
def list_sum (xs : list,ys: list) -> list:
    result = []
    for i in range(len(xs)):
        result.append(xs[i]+ys[i])
    return result


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]