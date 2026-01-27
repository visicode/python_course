class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(ils: list)->list:
    def passing(ca: CourseAttempt)->bool:
        return ca.grade > 0
    return list(filter(passing, ils))

def attempts_with_grade(ils: list, grade: int):
    def matching(ca: CourseAttempt)->bool:
        return ca.grade == grade
    return list(filter(matching, ils))

def passed_students(ils: list, crs: str)->list:
    mls = accepted(ils)
    def match(ca: CourseAttempt)->bool:
        return ca.course_name == crs
    return sorted(list(map(lambda elem: elem.student_name, filter(match,mls))))

