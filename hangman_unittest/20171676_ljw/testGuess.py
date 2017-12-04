import unittest

from guess import Guess

class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')
        self.g2 = Guess('test')
        self.g3 = Guess('about')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testGuess(self):
        self.assertTrue(self.g3.guess('t'))
        self.assertFalse(self.g3.guess('s'))
        self.assertTrue(self.g3.guess('a'))
        self.assertFalse(self.g3.guess('c'))

    def testFinished(self):
        self.g2.guess('t')
        self.g2.guess('e')
        self.g2.guess('s')
        self.assertTrue(self.g2.finished())

        self.g3.guess('a')
        self.g3.guess('b')
        self.g3.guess('o')
        self.g3.guess('u')
        self.g3.guess('t')
        self.assertTrue(self.g3.finished())


if __name__ == '__main__':
    unittest.main()
