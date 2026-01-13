# Write your solution here
fn = 'dictionary.txt'

my_dict={}
with open(fn) as my_file:
    for line in my_file:
        fin,eng=line.strip().split(";")
        my_dict[fin]=eng

while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    inp = input("Function: ")
    if inp=="1":
        fin = input("The word in Finnish: ")
        eng = input("The word in English: ")
        my_dict[fin]=eng

        with open(fn,"a") as my_file:
            my_file.write(f"{fin};{eng}\n")

        print("Dictionary entry added")

    elif inp=="2":
        st = input("Search term: ")
        for fin,eng in my_dict.items():
            if (fin.find(st)!=-1) or (eng.find(st)!=-1):
                print(f"{fin} - {eng}")

    elif inp=="3":
        print("Bye!")
        break