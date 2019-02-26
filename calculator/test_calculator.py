import unittest
import calculator

class TestStringMethods(unittest.TestCase):

    def testAddTest(self):
        self.assertEqual(calculator.add(3,6),9)
        self.assertEqual(calculator.add(4,-2),2)
        self.assertEqual(calculator.add(-6,6), 0)

    def testSubtractTest(self):
        self.assertEqual(calculator.subtract(3,6),-3)
        self.assertEqual(calculator.subtract(4,-2),6)
        self.assertEqual(calculator.subtract(-6,6), -12)

    def testMultiplyTest(self):
        self.assertEqual(calculator.multiply(3,6),18)
        self.assertEqual(calculator.multiply(4,-2),-8)
        self.assertEqual(calculator.multiply(-6,6), -36)

    def testDivideTest(self):
        self.assertEqual(calculator.divide(6,3),2)
        self.assertEqual(calculator.divide(4,-2),-2)
        self.assertEqual(calculator.divide(-6,6), -1)

    

    def testPowerTest(self):
        self.assertEqual(calculator.power(2,2),4)
        self.assertEqual(calculator.power(3,3),27)
        self.assertEqual(calculator.power(-6,2), 36)

   
        if __name__ == '__main__':
           unittest.main()

          
          
          
#command to run the unit test
#C:\Users\siban\source\repos\Python\CIS104\calculator>python -m unittest test_calculator.py
