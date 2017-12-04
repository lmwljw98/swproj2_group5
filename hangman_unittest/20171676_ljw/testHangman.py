import unittest

from hangman import Hangman


class TestGuess(unittest.TestCase):
    def setUp(self):
        self.t1 = Hangman()

    def testDecreaseLife(self):
        self.t1.decreaseLife()
        self.assertEqual(self.t1.remainingLives, 5)
        self.t1.decreaseLife()
        self.assertEqual(self.t1.remainingLives, 4)
        self.t1.decreaseLife()
        self.assertEqual(self.t1.remainingLives, 3)
        self.t1.decreaseLife()
        self.assertEqual(self.t1.remainingLives, 2)
        self.t1.decreaseLife()
        self.assertEqual(self.t1.remainingLives, 1)
        self.t1.decreaseLife()
        self.assertEqual(self.t1.remainingLives, 0)


if __name__ == '__main__':
    unittest.main()
