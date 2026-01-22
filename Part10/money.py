# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __eq__(self, another):
        return (self.__cents==another.__cents) and (self.__euros==another.__euros)

    def __ne__(self, another):
        return (self.__cents!=another.__cents) or (self.__euros!=another.__euros)

    def __gt__(self, another):
        if self.__euros>another.__euros:
            return True
        elif self.__euros==another.__euros:
            return self.__cents>another.__cents
        return False

    def __lt__(self, another):
        if self.__euros<another.__euros:
            return True
        elif self.__euros==another.__euros:
            return self.__cents<another.__cents
        return False

    def __add__(self,another):
        c=0
        e=0
        m=0 #carry
        if self.__cents+another.__cents>=100:
            c=self.__cents+another.__cents-100
            m=1
        else:
            c=self.__cents+another.__cents
        e=self.__euros+another.__euros+m
        return Money(e,c)

    def __sub__(self,another):
        c=0
        e=0
        m=0 #carry
        if self<another:
            raise ValueError("a negative result is not allowed")
        if self.__cents-another.__cents<0:
            c=100+self.__cents-another.__cents
            m=1
        else:
            c=self.__cents-another.__cents
        e=self.__euros-m-another.__euros
        return Money(e,c)

