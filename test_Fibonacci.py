import unittest   #built-in module
import Fibonacci  # our custom module

'''  boolean   is  | is not
     None      is  none 
'''
class TestFibonacci(unittest.TestCase):    # case number 1
    def test_fibonacci_with_positive_input(self):
        number=10
        result=Fibonacci.get_fibonacci_series(number)
        assert result==[0,1,1,2,3,5,8,13,21,34]
        
        number=5
        result=Fibonacci.get_fibonacci_series(number)
        assert result==[0,1,1,2,3]
        
        
    
    def test_fibonacci_with_zero_input(self):
        number=0
        result= Fibonacci.get_fibonacci_series(number)
        assert result is None
        
    def test_fibonacci_with_one_input(self):
        number =1
        result=Fibonacci.get_fibonacci_series(number)
        assert result ==[0]
         
         
    def test_fibonacci_with_wrong_input(self):
        number=0.1
        result=Fibonacci.get_fibonacci_series(number)
        assert result is None

       
unittest.main ()      