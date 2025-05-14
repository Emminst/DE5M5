import unittest
from calculator_app import Calculator

class TestOperations(unittest.TestCase):

    def setUp(self):
        self.calculation=Calculator(8,2)  #removes the need for repeating this in every test below

    def test_sum(self):
        #calculation = Calculator(8,2)
        #self.assertEqual(calculation.do_sum(),10,'The sum is wrong (not 10)!')
        #but need to add 'self.' before calculation now:
        self.assertEqual(self.calculation.do_sum(),10,'The sum is wrong (not 10)!')

    def test_product(self):
        #calculation = Calculator(8,2)
        #self.assertEqual(calculation.do_product(),16,'The product is wrong (not 16)!')   
        #but need to add 'self.' before calculation now:
        self.assertEqual(self.calculation.do_product(),16,'The product is wrong (not 16)!')

    def test_subtract(self):
        #calculation = Calculator(8,2)
        #self.assertEqual(calculation.do_subtract(),6,'The difference is wrong (not 6)!')         
        #but need to add 'self.' before calculation now:
        self.assertEqual(self.calculation.do_subtract(),6,'The difference is wrong (not 6)!')

    def test_divide(self):
        #calculation = Calculator(8,2)
        #self.assertEqual(calculation.do_divide(),4,'The quotient is wrong (not 4)!')   
        #but need to add 'self.' before calculation now:
        self.assertEqual(self.calculation.do_divide(),4,'The quotient is wrong (not 4)!')

if __name__ == '__main__':
    unittest.main()

