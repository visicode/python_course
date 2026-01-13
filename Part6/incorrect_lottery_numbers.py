# Write your solution here
def filter_incorrect():
    fn='lottery_numbers.csv'
    of='correct_numbers.csv'
    my_dict={}
    with open(fn) as ifile:
        for line in ifile:
            invalid = False
            if line.find(";")!=-1:
                week,numbers=line.strip().lower().split(";")

                #check week
                txt,wn = week.split(" ")
                if not wn.isdecimal():
                    invalid=True
                
                #read numbers list as string
                num_sls=[] #string
                num_ls=[] #int
                st=""
                for c in numbers:
                    if c!=",":
                        st+=c
                    else:
                        num_sls.append(st)
                        st=""
                   
                if st!="": #last number to add (it does not have adter a coma)                        
                    num_sls.append(st)

                #check and convert only numbers in the list
                for num in num_sls:
                    #print(f"{num} {num.isdecimal()}")
                    if num.isdecimal():
                        num_ls.append(int(num))
                    else:
                        invalid=True
                        
                
                #check if there is enough numbers
                if len(num_ls)<7:
                    invalid=True

                if (min(num_ls)<1) or (max(num_ls)>39):
                    invalid=True
                
                for num in num_ls:
                    if num_ls.count(num)>1:
                        invalid=True
                
                if not invalid:
                    my_dict[week]=numbers

    
    with open(of,"w") as ofile:
        for week,nums in my_dict.items():
            ofile.write(f"{week};{nums}\n")



if __name__ == '__main__':
    filter_incorrect()