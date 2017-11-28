from word import Word
from hangman import Hangman
from guess import Guess


class Game:
    def __init__(self):
        self.word = Word('words.txt')
        self.guess = Guess(self.word.randFromDB())
        self.hangman = Hangman()
        self.finished = False
        self.maxTries = self.hangman.getLife()

    def play(self):
        while self.guess.failed < self.maxTries:
            display = self.hangman.get(self.maxTries - self.guess.failed)
            print(display)
            print(self.guess.display())
            print(" ".join(self.guess.usedList))

            character = input("input character: ")
            if len(character) != 1:
                print('One character at a time!')
                continue
            if character in self.guess.usedList:
                print("\'%s\' has been already used" % character)
                continue

            self.finished = self.guess.guess(character)
            if self.finished:
                break

        if self.finished:
            print("Success")
        else:
            display = self.hangman.get(self.maxTries - self.guess.failed)
            print(display)
            print(self.guess.display())
            print(" ".join(self.guess.usedList))
            print("fail")


if __name__ == "__main__":
    game = Game()
    game.play()
