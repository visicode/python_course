# tee ratkaisusi tänne
class Course:
    def __init__(self, name: str, grade: int, credit: int):
        if name=="":
            raise ValueError("Course Name cannot be empty")
        if grade<1 or grade>5:
            raise ValueError("Grade should be between 1-5")
        if credit<0 or credit>10:
            raise ValueError("Credit should be between 1-10")
        self.__name=name
        self.__grade=grade
        self.__credit=credit

    @property
    def grade(self):
        return self.__grade
    @grade.setter
    def grade(self, grade: int):
        self.__grade=grade
    @property
    def credit(self):
        return self.__credit

class Courses:
    def __init__(self):
        self.__courses = {}

    def add_course(self, name: str, grade: int, credit: int):
        if name =="":
            raise ValueError("Course Name cannot be empty")
        if not name in self.__courses:
            self.__courses[name] = Course(name,grade,credit)
            return
        if grade>self.__courses[name].grade:
            self.__courses[name].grade=grade

    def get_course(self, name: str)->str:
        if name =="":
            raise ValueError("Course Name cannot be empty")
        if not name in self.__courses:
            return "no entry for this course"
        return f"{name} ({self.__courses[name].credit} cr) grade {self.__courses[name].grade}"
    
    def get_grade(self,name:str)->int:
        if name =="":
            raise ValueError("Course Name cannot be empty")
        if not name in self.__courses:
            return "no entry for this course"
        return self.__courses[name].grade

    def get_credit(self,name:str)->int:
        if name =="":
            raise ValueError("Course Name cannot be empty")
        if not name in self.__courses:
            return "no entry for this course"
        return self.__courses[name].credit

    def all_entries(self):
        return self.__courses

class CourseRecordsApplication:
    def __init__(self):
        self.__records = Courses()

    def help(self):
        print("commands: ")
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_course(self):
        name = input("course: ")
        grade = int(input("grade: "))
        credit = int(input("credits: "))
        self.__records.add_course(name, grade, credit)

    def get_course(self):
        name = input("course: ")
        print(self.__records.get_course(name))
        #ItP (5 cr) grade 3

    
    def stats(self):
        l = len(self.__records.all_entries())
        s_gr=0
        s_cr=0
        dic={}
        for i in range(6):
            dic[i]=0

        for c in self.__records.all_entries():
            s_cr+=self.__records.get_credit(c)
            s_gr+=self.__records.get_grade(c)
            dic[self.__records.get_grade(c)]+=1
        
        print (f"{l} completed courses, a total of {s_cr} credits")
        print (f"mean {s_gr/l:.1f}")
        print ("grade distribution")
        for i in range(5,0,-1):
            print(f"{i}:","x"*dic[i])

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_course()
            elif command == "2":
                self.get_course()
            elif command == "3":
                self.stats()
            else:
                self.help()

myapp=CourseRecordsApplication()
myapp.execute()