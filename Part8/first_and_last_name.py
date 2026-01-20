# Write your solution here:
class Person:
    
    def __init__(self, name: str):
        self.name = name

    def return_first_name(self) -> str:
        res=""
        pos = self.name.find(' ')
        if pos!=-1:
            res=self.name[:pos]
        
        return(res)

    def return_last_name(self) -> str:
        res=""
        pos = self.name.find(' ')
        if pos!=-1:
            res=self.name[pos+1:]
        
        return(res)


if __name__ == "__main__":
    peter = Person("Peter Pythons")
    print(peter.return_first_name())
    print(peter.return_last_name())

    paula = Person("Paula Pythonnen")
    print(paula.return_first_name())
    print(paula.return_last_name())











