import random


class Word:
    def __init__(self, filename):
        f = open(filename, 'r')
        self.words = f.readlines()
        f.close()

        self.count = len(self.words)

        print('%d words in DB' % self.count)

    def test(self):
        return 'default'

    def randFromDB(self):
        r = random.randrange(self.count)
        return self.words[r].rstrip()
