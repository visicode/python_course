# WRITE YOUR SOLUTION HERE:

class BankAccount:
    def __init__(self,owner :str, account_number: str, balance :float ):
        self.__balance=0
        if owner != '' and account_number != '':
            self.__owner=owner
            self.__account_number = account_number
            if balance >= 0:
                self.__balance = balance
            else:
                raise ValueError("Opening balance cannot be negative")
        else:
            raise ValueError("Owner and/or Account Number cannot be empty")
    
    def deposit(self, amount: float):
        if amount>0:
            self.__balance+=amount
            self.__service_charge()

    def withdraw(self, amount: float):
        if self.__balance>=amount:
            self.__balance-=amount
            self.__service_charge()

    @property
    def balance(self):
        return self.__balance

    def __service_charge(self):
        ch = round(self.__balance/100,2) # in money the smallest is 1 cent (no further decimals)
        self.__balance-=ch
        
