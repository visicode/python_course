class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(ils: list)->list:
    def orl (elem: ClimbingRoute)->int:
        return elem.length
    return sorted(ils, key=orl,reverse=True)

def sort_by_difficulty(ils: list)->list:
    def org (elem: ClimbingRoute)->tuple:
        return (elem.grade,elem.length)
    return sorted(ils, key=org,reverse=True)

