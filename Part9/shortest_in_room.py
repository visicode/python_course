# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons=[]
        
    def add (self, person: Person):
        if person!=None:
            self.persons.append(person)

    def is_empty(self) -> bool:
        return len(self.persons)==0
    
    def print_contents(self):
        if not self.is_empty():
            s=0
            for pr in self.persons:
                s+=pr.height
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {s} cm")
            for pr in self.persons:
                print(f"{pr.name} ({pr.height} cm)")

    def shortest(self)->Person:
        if self.is_empty():
            return None
        shorty=self.persons[0]
        for pr in self.persons:
            if pr.height < shorty.height:
                shorty=pr
        return shorty

    def remove_shortest(self)->Person:
        if self.is_empty():
            return None
        shorty = self.shortest()
        self.persons.remove(shorty)
        return shorty

