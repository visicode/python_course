# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.number =  []

    def add_number(self, number:int):
        self.number.append(number)
        self.numbers+=1

    def count_numbers(self):
        return(self.numbers)
    
    def get_sum(self):
        res=0
        if self.numbers>0:
            res=sum(self.number)
        return res
    
    def average(self):
        res=0
        if self.numbers>0:
            s=sum(self.number)
            res=s/self.numbers
        return res

stats = NumberStats()
odd_stats = NumberStats()
even_stats = NumberStats()
print("Please type in integer numbers: ")

while(True):
    inp = input()
    if inp == '-1':
        break
    stats.add_number(int(inp))

    if int(inp)%2==0:
        even_stats.add_number(int(inp))
    else:
        odd_stats.add_number(int(inp))

print("Sum of numbers:", stats.get_sum())
print("Mean of numbers:", stats.average())
print("Sum of even numbers:",even_stats.get_sum())
print("Sum of odd numbers:",odd_stats.get_sum())
