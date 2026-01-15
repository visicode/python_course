from string import ascii_uppercase

# Write your solution here
def run(prg: list)->list:
    ret=[]
    var={}

    for c in ascii_uppercase:
        var[c]=0

    pc=0 #program counter :-)

    while pc!=len(prg): #we run out of codes then finnish

        line=prg[pc]

        if line[:3]=='MOV':
            par1=line[4]
            par2=line[6:]
            if par2 in ascii_uppercase:
                val=var[par2]
            else:
                val=int(par2)
            var[par1]=val

            
        elif line[:5]=='PRINT':
            par2=line[6:]
            if par2 in ascii_uppercase:
                val=var[par2]
            else:
                val=int(par2)
            ret.append(val)
            
        elif line[:3]=='ADD':
            par1=line[4]
            par2=line[6:]
            if par2 in ascii_uppercase:
                val=var[par2]
            else:
                val=int(par2)
            var[par1]+=val

        elif line[:3]=='SUB':
            par1=line[4]
            par2=line[6:]
            if par2 in ascii_uppercase:
                val=var[par2]
            else:
                val=int(par2)
            var[par1]-=val

        elif line[:3]=='MUL':
            par1=line[4]
            par2=line[6:]
            if par2 in ascii_uppercase:
                val=var[par2]
            else:
                val=int(par2)
            var[par1]*=val

        elif line[:3]=='END':
            return ret
        
        elif line[:2]=='IF':
            line_ls = line.split(" ")
            #['IF', 'A', '==', '2', 'JUMP', 'forward']
            par1=line_ls[1]
            par2=line_ls[3]
            comp=line_ls[2]
            loc=line_ls[5]

            if par1 in ascii_uppercase:
                val1=var[par1]
            else:
                val1=int(par1)

            if par2 in ascii_uppercase:
                val2=var[par2]
            else:
                val2=int(par2)

            eval=False
            #==, !=, <, <=, >, >=
            if comp=='==':
                if val1==val2:
                    eval=True
            if comp=='!=':
                if val1!=val2:
                    eval=True
            if comp=='<':
                if val1<val2:
                    eval=True
            if comp=='<=':
                if val1<=val2:
                    eval=True
            if comp=='>':
                if val1>val2:
                    eval=True
            if comp=='>=':
                if val1>=val2:
                    eval=True
            
            if eval:
                #jump location
                for i in range(len(prg)):
                    #print (i, prg[i])
                    if prg[i].find(loc+":")!=-1:
                        #print(pc,i)
                        pc=i

        elif line[:4]=='JUMP':
            loc = line[4:].strip()
            #print (loc)
            for i in range(len(prg)):
                #print (i, prg[i])
                if prg[i].find(loc+":")!=-1:
                    #print(pc,i)
                    pc=i

        #print(pc)

        pc+=1

    return ret


if __name__ == '__main__':
    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)