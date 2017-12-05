import unittest
from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ _ _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd _ _ a u _ t ')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('a')  # used char
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('z')  # incorrect char
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u l t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a t u ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' a d t u ')
        self.g1.guess('e')
        self.assertEqual(self.g1.displayGuessed(), ' a d e t u ')
        self.g1.guess('a')  # used char
        self.assertEqual(self.g1.displayGuessed(), ' a d e t u ')
        self.g1.guess('z')  # incorrect char
        self.assertEqual(self.g1.displayGuessed(), ' a d e t u z ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayGuessed(), ' a d e l t u z ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayGuessed(), ' a d e f l t u z ')

    def testGuess(self):
        self.assertTrue(self.g1.guess('a'))
        self.assertTrue(self.g1.guess('t'))
        self.assertTrue(self.g1.guess('u'))
        self.assertTrue(self.g1.guess('d'))
        self.assertTrue(self.g1.guess('e'))
        self.assertTrue(self.g1.guess('a'))     # used char
        self.assertFalse(self.g1.guess('z'))    # incorrect char
        self.assertTrue(self.g1.guess('l'))
        self.assertTrue(self.g1.guess('f'))

    def testFinished(self):
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')
        self.assertFalse(self.g1.finished())
        self.g1.guess('t')
        self.assertFalse(self.g1.finished())
        self.g1.guess('u')
        self.assertFalse(self.g1.finished())
        self.g1.guess('d')
        self.assertFalse(self.g1.finished())
        self.g1.guess('e')
        self.assertFalse(self.g1.finished())
        self.g1.guess('a')  # used char
        self.assertFalse(self.g1.finished())
        self.g1.guess('z')  # incorrect char
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertTrue(self.g1.finished())


if __name__ == '__main__':
    unittest.main()
