class Guess:
    def __init__(self, word):
        self.word = word
        self.usedList = []
        self.failed = 0
        self.tries = 0
        self.status = "_" * len(self.word)

    def display(self):
        return self.status

    def getFailed(self):
        return self.failed

    def guess(self, character):
        self.tries += 1
        if character in self.word:
            newStr = ""
            for i in range(len(self.word)):
                if character == self.word[i]:
                    newStr += character
                else:
                    newStr += self.status[i]
            self.status = newStr
            self.usedList.append(character)
            if self.status == self.word:
                return True
            else:
                return False
        else:
            self.usedList.append(character)
            self.failed += 1
            return False


if __name__ == "__main__":
    a = Guess("paper")
    print(a.guess("a"), a.status)
    print(a.guess("p"), a.status)
    print(a.guess("e"), a.status)
    print(a.guess("r"), a.status)
