import unittest
from sqrt import lazy_sqrt, builtin_sqrt, newton_sqrt1


class SqrtTest(unittest.TestCase):
    '''obligatory docstring, tests square root functions'''
    def test_sqrt9(self):
        self.assertEqual(newton_sqrt1(9), 3)
        self.assertEqual(lazy_sqrt(9), 3)

    def test_sqrt2(self):
        '''testing assertionAlmostEqual using for sqrt functions'''
        self.assertAlmostEqual(lazy_sqrt(2), builtin_sqrt(2))

if __name__ == '__main__':
    unittest.main()
