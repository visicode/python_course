# write your solution here
def largest()->int:
    with open("numbers.txt") as new_file:
        lg = 0

        for line in new_file:
            num = int(line)
            if num>lg:
                lg=num

    #print("Largest: ", lg)
    return lg

if __name__ == '__main__':
    largest()