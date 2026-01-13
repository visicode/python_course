# Write your solution here
def store_personal_data(person: tuple):
    fn="people.csv"

    #person:
    #Name (string)
    #Age (integer)
    #Height (float)

    with open(fn,"a") as my_file:
        my_file.write(f"{person[0]};{person[1]};{person[2]}\n")
