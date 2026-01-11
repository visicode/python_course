# Write your solution here
def anagrams(xs :str,ys: str) -> bool:
    if len(xs)!=len(ys):
        return False
    
    for i in range(len(xs)):
        if sorted(xs)[i]!=sorted(ys)[i]:
            return False
    return True

if __name__ == "__main__":
    print(anagrams("tame", "meta")) # True
    print(anagrams("tame", "mate")) # True
    print(anagrams("tame", "team")) # True
    print(anagrams("tabby", "batty")) # False
    print(anagrams("python", "java")) # False