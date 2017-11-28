class Guess:

    def __init__(self, word):
        self.secretWord = word
        self.guessedChars = set()
        self.numTries = 0
        self.currentStatus = "_"*len(self.secretWord)

    def display(self):
        print("Number of correct answers:" + self.currentStatus)
        print("Number of failures:%d"%self.numTries)

    def guess(self, character):
        self.char = character
        self.guessedChars.add(self.char)
        wordString = ''

        if self.char in self.secretWord:
            for i in range(len(self.currentStatus)):
                if self.secretWord[i] == self.char:
                    wordString += self.char
                elif self.currentStatus != "_":
                    wordString += self.currentStatus[i]
                else:
                    wordString += "_"
            self.currentStatus = wordString
        else:
            self.numTries += 1

        if self.secretWord == self.currentStatus:
            return True