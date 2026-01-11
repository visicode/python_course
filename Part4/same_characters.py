# Write your solution here
def same_chars(txt,a,b):
    l=len(txt)
    if (a<0) or (b<0) or (a>=l) or (b>=l):
        return False
    elif txt[a]==txt[b]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))