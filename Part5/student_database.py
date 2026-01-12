# Write your solution here
def add_student (d: dict,u: str)->None:
    if u not in d:
        d[u]=[]

def print_student(d: dict, u: str)->None:
    if u not in d:
        print(f"{u}: no such person in the database")
    elif d[u]==[]:
        print(f"{u}:")
        print(" no completed courses")
    else:
        print(f"{u}:")
        info=d[u]
        l=len(info)
        sm=0
        print(f" {l} completed courses:")
        for i in info:
            print(f"  {i[0]} {i[1]}")
            sm+=i[1]
        print(f" average grade {sm/l:.1f}")


def add_course(d: dict,u: str,tp: tuple)->None:
    if u in d:
        if tp[1]<1:
            return
        found=False
        mod=False
        elem=()
        for i in d[u]:
            if (i[0]==tp[0]):
                if (i[1]>=tp[1]):
                    return
                else:
                    found=True
                    mod=True
                    elem = i
                    #we need to overwrite the old grade

        if mod:
            d[u].remove(elem)
            d[u].append(tp)

        if not found:
            d[u].append(tp)

def summary(d: dict)->None:
    if len(d)!=0:
        print(f"students {len(d)}")
        most = 0
        m_name = ""
        avg = 0
        b_name = ""
        for st in d:
            t=0
            if len(d[st])>most:
                most = len(d[st])
                m_name = st
            for el in d[st]:
                t+=el[1]
            if t/len(d[st])>avg:
                avg=t/len(d[st])
                b_name = st
        print(f"most courses completed {most} {m_name}")
        print(f"best average grade {avg} {b_name}")


if __name__=='__main__':
    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Data Structures and Algorithms", 5))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    print_student(students, "Peter")
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Eliza")

    summary(students)