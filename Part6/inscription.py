from os.path import exists
# Write your solution here

name = input("Whom should I sign this to: ")
fn = input("Where shall I save it: ")

if not(exists(fn)):
    with open(fn,"w") as new_file:
        new_file.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")


