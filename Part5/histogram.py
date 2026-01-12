# Write your solution here

def histogram(word: str):
    letters={}
    for letter in word:
        if letter not in letters:
            letters[letter] = "" #create key if not exists
        letters[letter]+="*"


    for key, value in letters.items():
        print(f"{key} {value}")

if __name__ == '__main__':
    histogram("statistically")