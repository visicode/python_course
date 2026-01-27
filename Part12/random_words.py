# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
    substrings = (characters[i : i + length] for i in range(amount))
    return substrings
