# Write your solution here

def filter_solutions()->None:
    co_fn="correct.csv"
    ico_fn="incorrect.csv"
    fn="solutions.csv"

    my_list=[]
    cor_ls=[]
    incor_ls=[]

    with open(fn) as orig_file:
        for line in orig_file:
            ls=line.strip().split(";")
            my_list.append(ls)
    #print(my_list)

    for user in my_list:
        #if we subtracting together
        if user[1].find("-")!=-1:
            arg1,arg2=user[1].split("-")
            sol=int(arg1)-int(arg2)
            if sol==int(user[2]):
                cor_ls.append(user)
            else:
                incor_ls.append(user)
        #if we adding together
        if user[1].find("+")!=-1:
            arg1,arg2=user[1].split("+")
            sol=int(arg1)+int(arg2)
            if sol==int(user[2]):
                cor_ls.append(user)
            else:
                incor_ls.append(user)

    with open(co_fn,"w") as cor_file:
        for line in cor_ls:
            cor_file.write(f"{line[0]};{line[1]};{line[2]}\n")

    with open(ico_fn,"w") as incor_file:
        for line in incor_ls:
            incor_file.write(f"{line[0]};{line[1]};{line[2]}\n")


if __name__ == '__main__':
    filter_solutions()