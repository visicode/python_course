# Write your solution here
def oldest_person(ls: list)->str:
    name=""
    year=9999
    for element in ls:
        if element[1]<year:
            year=element[1]
            name=element[0]
    return name


if __name__=='__main__':
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))