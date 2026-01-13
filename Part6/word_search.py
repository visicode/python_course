# Write your solution here
def find_words(search_term: str)->list:
    res=[]
    fn='words.txt'

    word_list=[]
    with open(fn) as wf:
        for line in wf:
            word_list.append(line.strip())

    if '*' in search_term:
        if search_term[0]=='*':
            for wo in word_list:
                if wo.endswith(search_term[1:]):
                    res.append(wo)
        else:
            for wo in word_list:
                if wo.startswith(search_term[:-1]):
                    res.append(wo)

    elif '.' in search_term:
        for wo in word_list:
            l = len(wo)
            ok=True
            if len(wo)!=len(search_term):
                ok=False
            else:
                for i in range(l):
                    #Only need to match the characters that are not dot
                    if search_term[i]!='.':
                        if search_term[i]!=wo[i]:
                            ok=False
            
            if ok :
                res.append(wo)

    #we do not have special chars so need to check exact match
    else:
        if search_term in word_list:
            res.append(search_term)

                
    return res

if __name__ == '__main__':
    print(find_words(".a.."))