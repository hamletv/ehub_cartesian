import unittest
from bcehub import *

class CartesianTests(unittest.TestCase):

    def test_bash_cartesianprod(self):
        self.assertEqual(bash_cartesianprod('a{b,c}d{e,f,g}hi'), ['abdehi', 'abdfhi', 'abdghi', 'acdehi', 'acdfhi', 'acdghi'])
        self.assertEqual(bash_cartesianprod('a{b{c{d,e,f}g}h}i'), ['abcdghi', 'abceghi', 'abcfghi'])
        self.assertEqual(bash_cartesianprod('a{8}'), ['a8'])
        self.assertEqual(bash_cartesianprod('abdcdef'), ['abdcdef'])
        self.assertEqual(bash_cartesianprod('{a,b}{c,d}{e,f}'), ['ace', 'acf', 'ade', 'adf', 'bce', 'bcf', 'bde', 'bdf'])
        with self.assertRaises(InvalidString):
            bash_cartesianprod('a{b,c}d{e,f,g}}}hi')

    def test_split_passed_str(self):
        self.assertEqual(split_passed_str('a,b,c,d'), ['a', 'b', 'c', 'd'])
        self.assertEqual(split_passed_str('a{b,c}d{e,f,g}hi'), ['a{b,c}d{e,f,g}hi'])
        with self.assertRaises(InvalidString):
            bash_cartesianprod('a{b,c}d{e,f,g}}}hi')

    def test_extract_char(self):
        self.assertEqual(extract_char('a{b,c}'), (['a', ''], [['b','c']]))
        self.assertEqual(extract_char('a{b,c}d{e,f,g}hi'), (['a', 'd', 'hi'], [['b', 'c'], ['e', 'f', 'g']]))
        self.assertEqual(extract_char('a{b{c{d{e{f,g,h}}}}}'), (['a', ''], [['b{c{d{e{f,g,h}}}}']]))
        with self.assertRaises(InvalidString):
            bash_cartesianprod('a{b,c}d{e,f,g}}}hi')
if __name__ == '__main__':
    unittest.main()
