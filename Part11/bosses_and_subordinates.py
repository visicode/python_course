# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)
    

def count_subordinates(ie: Employee)->int:
    ret=0
    if len(ie.subordinates)==0:
        return 0
    for i in ie.subordinates:
        ret=ret+1+count_subordinates(i)
    return ret

