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
        if len(player1_word) > len(player2_word):
            return 1
        elif len(player2_word) > len(player1_word):
            return 2

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = 'aeiou'
        c1, c2 = 0, 0
        for vowel in vowels:
            c1 += player1_word.count(vowel)
            c2 += player2_word.count(vowel)
        if c1 > c2:
            return 1
        elif c2 > c1:
            return 2

class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        valid_input = ['rock', 'paper', 'scissors']
        if player1_word.lower() not in valid_input and player2_word.lower() in valid_input:
            return 2
        elif player1_word.lower() in valid_input and player2_word.lower() not in valid_input:
            return 1
        elif not (player1_word.lower() in valid_input and player2_word.lower() in valid_input) or player1_word.lower() == player2_word.lower():
            return
        elif player1_word.lower() == 'rock' and player2_word.lower() == 'scissors':
            return 1
        elif player1_word.lower() == 'scissors' and player2_word.lower() == 'paper':
            return 1
        elif player1_word.lower() == 'paper' and player2_word.lower() == 'rock':
            return 1
        else:
            return 2
        
if __name__ == "__main__":
    p = MostVowels(3)
    p.play()

