# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self,day: int,month: int, year: int):
        if 30<day or day<1 or 12<month or month<1 or year<0 or year>9999:
            raise ValueError("Invalide date")
        
        self.__day=day
        self.__month=month
        self.__year=year

    @property
    def day(self):
        return self.__day
    
    @day.setter
    def day(self, day:int):
        if day<0 or day>30:
            raise ValueError("Invalid Day value")
        self.__day=day
    
    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, month:int):
        if month<0 or month>12:
            raise ValueError("Invalid Month value")
        self.__month=month
    
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year:int):
        if year<0 or year>9999:
            raise ValueError("Invalid Year value")
        self.__year=year

    def __str__(self):
        return f"{self.__day}.{self.__month}.{self.__year}"
    
    def __eq__(self, value):
        return (self.__day==value.__day) and (self.__month==value.__month) and (self.__year==value.__year)
    
    def __nq__(self, value):
        return (self.__day!=value.__day) or (self.__month!=value.__month) or (self.__year!=value.__year)
    
    def __gt__(self, value):
        if self.__year>value.__year:
            return True
        elif (self.__year==value.__year) and (self.__month>value.__month):
            return True
        elif (self.__year==value.__year) and (self.__month==value.__month) and (self.__day>value.__day):
            return True
        return False

    def __lt__(self, value):
        if self.__year<value.__year:
            return True
        elif (self.__year==value.__year) and (self.__month<value.__month):
            return True
        elif (self.__year==value.__year) and (self.__month==value.__month) and (self.__day<value.__day):
            return True
        return False

    def __add__(self, day:int):
        td=0
        tm=0
        ty=0
        d =0
        m =0
        y =0
        if day>=360:
            ty=day//360
        temp=day%360
        if temp>=30:
            tm=temp//30
        td=temp%30

        cd=0 #carry
        cm=0
        if self.__day+td>30:
            d=self.__day+td-30
            cd=1
        else:
            d=self.__day+td
        if self.__month+tm+cd>12:
            m=self.__month+tm+cd-12
            cm=1
        else:
            m=self.__month+tm+cd
        y=self.__year+ty+cm
        return SimpleDate(d,m,y)

    def __sub__(self, another)->int:
        data1=self.__year*360+self.__month*30+self.__day
        data2=another.__year*360+another.__month*30+another.__day

        if data1-data2<0:
            return data2-data1
        return data1-data2
