# Write your solution here
def sum_of_positives(ls :list) -> int:
    result = 0
    for i in ls:
        if i>0:
            result+=i
    return result