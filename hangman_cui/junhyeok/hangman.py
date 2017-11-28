class Hangman:
    text = [

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |   /
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|\\
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |   /|
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |    |
  |    |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |    o
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

'''\
   ____
  |    |
  |
  |
  |
  |
 _|_
|   |______
|          |
|__________|\
''',

    ]

    def getLife(self):
        return len(self.text) - 1

    def get(self, life):
        if life >= len(self.text):
            return self.text[-1]
        else:
            return self.text[life]


if __name__ == "__main__":
    man = Hangman()
    for i in range(7, -1, -1):
        print(man.get(i))

