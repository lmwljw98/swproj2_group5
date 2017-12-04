import unittest

from word import Word


class TestGuess(unittest.TestCase):
    def setUp(self):
        self.t1 = Word('words.txt')

    def testTest(self):
        self.assertEqual(self.t1.test(), 'aback')

if __name__ == '__main__':
    unittest.main()
