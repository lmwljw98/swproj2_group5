import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        currentList = ['d', 'e', 'f', 'a', 'u', 'l', 't']
        currentString = ""
        currentStringList = ["_", "_", "_", "_", "_", "_", "_"]

        for i in range(len(currentList)):
            self.g1.guess(currentList[i])
            currentStringList[i] = currentList[i]
            for j in range(len(currentStringList)):
                currentString = currentString + currentStringList[j] + " "
            self.assertEqual(self.g1.displayCurrent(), currentString)


    def testDisplayGuessed(self):
        currentList = ['d', 'e', 'f', 'a', 'u', 'l', 't']
        currentString = " "
        currentStringList = ['n']

        for i in range(len(currentList)):
            self.g1.guess(currentList[i])
            currentStringList.append(currentList[i])
            currentStringList = sorted(currentStringList)
            for j in range(len(currentStringList)):
                currentString = currentString + currentStringList[j] + " "
            self.assertEqual(self.g1.displayGuessed(), currentString)


if __name__ == '__main__':
    unittest.main()
