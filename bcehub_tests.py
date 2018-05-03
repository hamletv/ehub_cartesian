import unittest
from bcehub import *

class CartesianTests(unittest.TestCase):

    def test_bash_cartesianprod(self):
        self.assertEqual(bash_cartesianprod('a{b,c}d{e,f,g}hi'), ['abdehi', 'abdfhi', 'abdghi', 'acdehi', 'acdfhi', 'acdghi'])
        self.assertEqual(bash_cartesianprod('a{b}'), ['ab'])
        self.assertEqual(bash_cartesianprod('a{8}'), ['a8'])
        self.assertEqual(bash_cartesianprod('abdcdef'), ['abdcdef'])
        self.assertEqual(bash_cartesianprod('{a,b}{c,d}{e,f}'), ['ace', 'acf', 'ade', 'adf', 'bce', 'bcf', 'bde', 'bdf'])

if __name__ == '__main__':
    unittest.main()
