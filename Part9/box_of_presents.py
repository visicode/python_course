# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self, name: str, weight: int):
        self.name=name
        self.weight=weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.present_list=[]

    def add_present(self, present: Present)->None:
        self.present_list.append(present)


    def total_weight(self) -> int:
        s=0
        for pr in self.present_list:
            s += pr.weight
        return s

    
