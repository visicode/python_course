# WRITE YOUR SOLUTION HERE:
class Car:
    def __init__(self):
        self.__odo = 0
        self.__tank = 0
    
    def fill_up(self):
        self.__tank=60

    def drive(self, km: int):
        if km>0 and self.__tank>0:
            if km<=self.__tank:
                self.__tank-=km
                self.__odo+=km
            else:
                self.__odo+=self.__tank
                self.__tank=0

    def __str__(self):
        return f"Car: odometer reading {self.__odo} km, petrol remaining {self.__tank} litres"        
 
#Car: odometer reading 0 km, petrol remaining 0 litres