
def balanced_brackets(my_string: str):
    ts=""
    # remove first non-brackets:
    for i in range(len(my_string)):
        if my_string[i] in '[(':
            ts=my_string[i:]
            break
        #reached end
        if i==len(my_string)-1:
            ts=my_string

    nts=""
    #remove back non-brackets:
    for i in range(len(ts)):
        if ts[-(i+1)] in ')]':
            if i==0:
                nts=ts
            else:
                nts=ts[:-(i+1)+1]
            break
        #reached end
        if i==len(ts)-1:
            nts=ts

    if len(nts) == 0:
        return True
    
    #check if no brackets left
    for i in range(len(nts)):
        if nts[i] in "[()]":
            break
        if i==len(nts)-1:
            return True

    if not ((nts[0] == '(' and nts[-1] == ')')  or (nts[0] == '[' and nts[-1] == ']') ):
        return False
    
    return balanced_brackets(nts[1:-1])


