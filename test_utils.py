# test_utils.py
# Author: Sébastien Combéfis
# Version: February 2, 2016

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(3),6)
        with self.assertRaises(ValueError):
            utils.fact(-1)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,2,-15),(-5,3))
        self.assertEqual(utils.roots(1,-2,1),(1))
        self.assertEqual(utils.roots(1,0,1),())
        pass
    
    def test_integrate(self):
        self.assertTrue(-1.34< utils.integrate('x ** 2 - 1', -1, 1) < -1.33)
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
