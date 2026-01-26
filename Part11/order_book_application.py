# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    counter =1

    def __init__ (self, description: str, programmer: str, workload: int):
        
        self.description=description
        self.programmer=programmer
        self.workload=workload
        self._is_finished = False
        self.id=Task.counter

        Task.counter+=1

    def is_finished(self):
        return self._is_finished
    
    def mark_finished(self):
        self._is_finished=True

    def __str__ (self):
        res=""
        if self.is_finished():
            res="FINISHED"
        else:
            res="NOT FINISHED"
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {res}"

class OrderBook:
    def __init__(self):
        self.orders=[]

    def all_orders(self)->list:
        return self.orders
    
    def add_order(self, description: str, programmer: str, workload: int):
        new_task=Task(description, programmer, workload)
        self.orders.append(new_task)

    def programmers(self)->list:
        prg=[]
        for order in self.orders:
            if order.programmer not in prg:
                prg.append(order.programmer)
        return prg
    
    def mark_finished(self, fid: int) -> bool:
        notin = True
        for order in self.orders:
            if order.id==fid:
                order.mark_finished()
                notin = False
        if notin:
            print("erroneous input")
        return notin

    def finished_orders(self):
        res=[]
        for order in self.orders:
            if order.is_finished():
                res.append(order)
        return res

    def unfinished_orders(self):
        res=[]
        for order in self.orders:
            if not (order.is_finished()):
                res.append(order)
        return res

    def status_of_programmer(self, prs: str)->tuple:
        if prs not in self.programmers():
            print("erroneous input")
        v1=0
        v2=0
        v3=0
        v4=0
        for order in self.finished_orders():
            if order.programmer==prs:
                v1+=1
                v2+=order.workload

        for order in self.unfinished_orders():
            if order.programmer==prs:
                v3+=1
                v4+=order.workload

        return(v1,v3,v2,v4)


def print_help():
    print(""" commands:
    0 exit
    1 add order
    2 list finished tasks
    3 list unfinished tasks
    4 mark task as finished
    5 programmers
    6 status of programmer""")

#if __name__ == '__main__':
if True:
    ob=OrderBook()
    print_help()
    while True:
        command = input("command: ")
        if command == "0":
            break
        elif command == "1":
            desc = input("description: ")
            txt = input("programmer and workload estimate: ")
            if txt.count(" ")!=1:
                print("erroneous input")
                continue
            prs, ess = txt.split()
            if not ess.isdecimal():
                print("erroneous input")
                continue
            ob.add_order(desc,prs,int(ess))
            print("added!")
        elif command == "2":
            ft = ob.finished_orders()
            if ft==[]:
                print("no finished tasks")
            else:
                for task in ft:
                    print(task)
        elif command == "3":
            ft = ob.unfinished_orders()
            if ft==[]:
                print("no unfinished tasks")
            else:
                for task in ft:
                    print(task)
        elif command == "4":
            ids = input("id: ")
            if not ids.isdecimal():
                print("erroneous input")
                continue
            res=ob.mark_finished(int(ids))
            if not res:
                print("marked as finished")
        elif command == "5":
            prl = ob.programmers()
            for prm in prl:
                print(prm)
        elif command == "6":
            prns = input("programmer: ")
            stat = ob.status_of_programmer(prns)
            if stat != (0,0,0,0):
                print(f"tasks: finished {stat[0]} not finished {stat[1]}, hours: done {stat[2]} scheduled {stat[3]}")
        else:
            print ("unknown command")
            print_help()
        print()

