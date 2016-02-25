'''
Created on Feb 24, 2016

@author: User
'''

import unittest

class SimpleTest(unittest.TestCase):
    
    def test1(self):
        a = 1;
        b = 1;
        self.assertEqual(a, b, "values aren't equal")
    
    def test2(self):
        a = 2;
        b = 1;
        self.assertGreater(a, b, "b is greater than a")
        

suite = unittest.TestLoader().loadTestsFromTestCase(SimpleTest)
unittest.TextTestRunner(verbosity=2).run(suite)