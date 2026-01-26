
def most_common_words(ifl, limit):
    with open(ifl) as f:
        ils=f.read()

    rem=ils.replace(".","").replace(",","") #remove dot and comma
    mls=rem.split() #create a list of words
    return {word : mls.count(word) for word in mls if mls.count(word)>=limit}

    
