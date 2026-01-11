# Write your solution here
def first_word(txt):
    ndx = txt.find(' ')
    return txt[:ndx]

def second_word(txt):
    ndx = txt.find(' ')
    txt = txt[ndx+1:]
    ndx = txt.find(' ')
    if ndx==-1:
        return(txt)
    else:
        return txt[:ndx]

def last_word(txt):
    ndx = txt.rfind(' ')
    return txt[ndx+1:]


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))