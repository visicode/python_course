# Write your solution here
from datetime import datetime, timedelta

milenium = datetime(1999,12,31)

da = int(input("Day: "))
mo = int(input("Month: "))
ye = int(input("Year: "))

delta = milenium - datetime(ye,mo,da) 

if delta < timedelta(0):
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {delta.days} days old on the eve of the new millennium.")