#Given a list of numbers, where every number shows up twice except for one number, find that one number.

# TEST PROGRAM : first Test Driven Development application
# NOT FINISHED...

import unittest 
from singleNumber import *

class myFirstTest(unittest.TestCase):
#    def test_hello(self):
#        self.assertEqual(hello_world(), 'hello world')
#    def test_isnumber(self):
#        self.assertIs(type(num), type(1))
    def test_functionArgType(self):
        self.assertIs(type(myArray), type([2, 3]))
    def test_functionReturnNum(self):
        self.assertIs(type(singleNumber(arr)), type(1))

if __name__ == '__main__':
    unittest.main()


#testArray = [4, 3, 2, 4, 1, 3, 2]