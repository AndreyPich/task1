import unittest


from test_fibonacci import TestFibonacci
from test_determinant import TestDeterminant


suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestFibonacci))
suite.addTest(unittest.makeSuite(TestDeterminant))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
