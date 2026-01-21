# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        if name!='':
            self.__name=name
        else:
            raise ValueError("Name cannot be empty")
        
        if weight>0:
            self.__weight=weight
        else:
            raise ValueError("Weight cannot be 0 or negative")
    def name(self)->str:
        return self.__name
    def weight(self)->int:
        return self.__weight
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight: int):
        if max_weight>0:
            self.__max_weight=max_weight
        else:
            raise ValueError("Max Weight cannot be 0 or negative")
        self.__items=[]
        self.__cur_weight=0

    def add_item(self, item: Item):
        if self.__cur_weight+item.weight()<=self.__max_weight:
            self.__items.append(item)
            self.__cur_weight+=item.weight()

    def weight(self) -> int:
        return self.__cur_weight
    
    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        if len(self.__items)==0:
            return None
        heavy=self.__items[0]
        for item in self.__items:
            if item.weight()>heavy.weight():
                heavy=item
        return heavy

    def __str__(self):
        if len(self.__items)!=1:
            return f"{len(self.__items)} items ({self.__cur_weight} kg)"
        else:
            return f"{len(self.__items)} item ({self.__cur_weight} kg)"
        
class CargoHold:
    def __init__(self,max_weight: int):
        if max_weight>0:
            self.__max_weight=max_weight
        else:
            raise ValueError("Max Weight cannot be 0 or negative")
        self.__items=[]
        self.__cur_weight=0

    def add_suitcase(self, item: Suitcase):
        if self.__cur_weight+item.weight()<=self.__max_weight:
            self.__items.append(item)
            self.__cur_weight+=item.weight()

    def print_items(self):
        for i in self.__items:
            i.print_items()

    def weight(self) -> int:
        return self.__cur_weight

    def __str__(self):
        if len(self.__items)!=1:
            return f"{len(self.__items)} suitcases, space for {self.__max_weight-self.__cur_weight} kg"        
        else:
            return f"{len(self.__items)} suitcase, space for {self.__max_weight-self.__cur_weight} kg"
