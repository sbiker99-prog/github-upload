'''
Created on 24.11.2020

@author: caronist
'''
import unittest
from ste_testdome.max_sum import MaxSum

class Test(unittest.TestCase):


    def test_MaxSum_01(self):
        tl = [ 5, 29, 7, 11, 2, 10 ] 
        obj = MaxSum()
        self.assertEqual(40, obj.calc(tl))

    def test_MaxSum_02(self):
        tl = [ 5, 29, 7, 12, 2, 10, 100, 40, 50, 45, 201, 200 ] 
        obj = MaxSum()
        self.assertEqual(401, obj.calc_max_efficient(tl))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()