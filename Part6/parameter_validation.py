# Write your solution here
def new_person(name: str, age: int)->tuple:
    res=()

    if name=="":
        raise ValueError("The name is an empty string")
    if name.find(" ")==-1:
        raise ValueError("The name contains less than 2 words")
    if len(name)>40:
        raise ValueError("The name is longer than 40 characters")
    if age<0:
        raise ValueError("The age is negative")
    if age>150:
        raise ValueError("The age is greater than 150")
    
    res=(name,age)
    return res
