# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testInvalidInputA(self): 
        self.assertEqual(classifyTriangle(201,5,2),'InvalidInput')
    
    def testInvalidInputB(self): 
        self.assertEqual(classifyTriangle(0,0,1),'InvalidInput')

    def testInvalidInputC(self): 
        self.assertEqual(classifyTriangle(13,-5,2),'InvalidInput')
    
    def testInvalidInputD(self): 
        self.assertEqual(classifyTriangle("hI",5,2),'InvalidInput')
    
    def testNotATriangle(self): 
        self.assertEqual(classifyTriangle(4,1,2),'NotATriangle')
        
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(4,3,5),'Right','4,3,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testIsoscelesTriangles(self): 
        self.assertEqual(classifyTriangle(1,2,2),'Isoceles','1,2,2 should be isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(2,3,4),'Scalene','2,3,4 should be scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

