# Write your solution here:

class RealProperty:
    def __init__(self, rooms: int , square_metres: int , price_per_sqm:int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm
    def bigger(self, another:"RealProperty")->bool:
        return self.square_metres>another.square_metres 
    def price_difference(self, another:"RealProperty")->int:
        res=0
        ps=self.square_metres*self.price_per_sqm
        pa=another.square_metres*another.price_per_sqm
        if ps-pa>0:
            res=ps-pa
        else:
            res=pa-ps
        return res
    def more_expensive(self, another:"RealProperty")->bool:
        ps=self.square_metres*self.price_per_sqm
        pa=another.square_metres*another.price_per_sqm
        if ps-pa>0:
            return True
        return False

