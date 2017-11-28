class Guess:
    def __init__(self, word):
        self.secretWord = word
        self.currentStatus = ["_"] * len(self.secretWord)
        self.guessedChars = []
        self.numTries = 0

    def display(self):
        print("Current: " + "".join(self.currentStatus))
        print("Tries: " + str(self.numTries))

    def guess(self, character):
        self.guessedChars.append(character)
        if character not in self.secretWord:
            self.numTries += 1
        else:
            index = [i for i, letter in enumerate(self.secretWord) if letter == character]
            for j in range(len(index)):
                self.currentStatus[index[j]] = character

        if "".join(self.currentStatus) == self.secretWord:
            return True

        return False
