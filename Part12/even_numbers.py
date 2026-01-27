# Write your solution here

def even_numbers (mi: int, ma: int)->int:
    if mi%2==0:
        start=mi
    else:
        start=mi+1
    for i in range(start,ma+1,2):
        yield i
