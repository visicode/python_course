from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(ils: list)->int:
    return reduce(lambda x,y :y+x, [elem.credits for elem in ils],0)

def sum_of_passed_credits(ils: list)->int:
    mls = list( filter(lambda ca: ca.grade>0, ils))
    return reduce(lambda x,y :y+x, [elem.credits for elem in mls] ,0)

def average(ils: list)->float:
    mls = list( filter(lambda ca: ca.grade>0, ils))
    sm =reduce(lambda x,y :y+x, [elem.grade for elem in mls] ,0)
    return sm / len(mls)

#does not pass if I write "reduce ("