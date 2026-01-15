# Write your solution here
import json

def print_persons(fn: str) -> None:

    with open(fn) as my_file:
        data = my_file.read()

    persons = json.loads(data)

    for person in persons:
        name = person["name"]
        age = person["age"]
        hobbies_ls = person["hobbies"]
        hobbies=""
        for hob in hobbies_ls:
            if hob == hobbies_ls[0]:
                hobbies=hobbies_ls[0]
            else:
                hobbies+=f", {hob}"

        print(f"{name} {age} years ({hobbies})")

    return


if __name__ == '__main__':
    print_persons("file1.json")

#Peter Pythons 27 years (coding, knitting)
#Jean Javanese 24 years (coding, rock climbing, reading)