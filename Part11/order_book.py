# Write your solution here:
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
    
    def mark_finished(self, fid: int):
        notin = True
        for order in self.orders:
            if order.id==fid:
                order.mark_finished()
                notin = False
        if notin:
            raise ValueError("Id not in the Orders list")

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
            raise ValueError("Given programmer has no Tasks")
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

