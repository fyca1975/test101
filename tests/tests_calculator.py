import unittest
from src.calculator import suma, resta, multiplica, div


class CalculatorTests(unittest.TestCase):

    def test_div(self):
        assert div(20, 2) == 10

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(20, 0) 


    def test_suma(self):
        assert suma(2, 3) == 5
        

    def test_resta(self):
        assert resta(4, 2) == 2
        

    def test_multiplica(self):
        assert multiplica(5, 8) == 40
    

        
    
