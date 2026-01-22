# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player1_word)<len(player2_word):
            return 2
        return 3

class MostVowels(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        vowels='aeiou'
        p1v = 0
        p2v = 0

        for c in player1_word:
            print (c, vowels)
            if c in vowels:
                p1v+=1

        for c in player2_word:
            if c in vowels:
                p2v+=1

        if p1v > p2v:
            return 1
        elif p1v < p2v:
            return 2
        return 3

class RockPaperScissors(WordGame):
    def __init__(self, rounds):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        words=['rock','paper','scissors']
        p1w = 0
        p2w = 0

        if player1_word.lower() not in words:
            p1w=-1
        if player2_word.lower() not in words:
            p2w=-1

    #wrong input handling
        if p1w==-1 and p2w==0:
            return 2
        elif p1w==0 and p2w==-1:
            return 1
        elif p1w==-1 and p2w==-1:
            return 3

    #correct input handling
        if player1_word.lower()=="rock":
            if player2_word.lower()=='scissors':
                return 1
            elif player2_word.lower()=='paper':
                return 2
            else: #both have rocks
                return 3

        if player1_word.lower()=="paper":
            if player2_word.lower()=='scissors':
                return 2
            elif player2_word.lower()=='rock':
                return 1
            else: #both have papers
                return 3

        if player1_word.lower()=="scissors":
            if player2_word.lower()=='paper':
                return 1
            elif player2_word.lower()=='rock':
                return 2
            else: #both have papers
                return 3
