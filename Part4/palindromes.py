# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!
def palindromes (txt: str) -> bool:
    l=len(txt)//2+1
    for i in range(l):
        if txt[i]!=txt[-(i+1)]:
            return False
    return True

while True:
    szo = input("Please type in a palindrome: ")
    if palindromes(szo):
        print(f"{szo}  is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

