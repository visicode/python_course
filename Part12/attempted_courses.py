class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

def names_of_students(attempts: list)->list:
    return list(map(lambda ca: ca.student_name, attempts))

def course_names(attempts: list)->list:
    res=[]
    mp = map(lambda ca: ca.course_name, attempts)
    [res.append(course) for course in mp if course not in res]
    return sorted(res)


#Part1 model solution does not return list
#Part2 tests did not check if returned list was sorted (mine wasn't and still passed)