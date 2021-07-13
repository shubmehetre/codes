import unittest
import sample_code1

class DivideNosTestcase(unittest.TestCase):
    """testing sample_code1.py - division of 2 nos"""

    # def __init__(self, methodName: str) -> None:
    #     super().__init__(methodName=methodName)

    def test_normal_nos(self):
        ans = sample_code1.divide_two_nos(10,5)
        self.assertEqual(ans, 2.0)
    
    def test_alphabets(self):
        ans = sample_code1.divide_two_nos(100, 50)
        self.assertEqual(ans, 2.0)

    # def test_divide_by_zero(self):
    #     ZeroDivisionError = sample_code1.divide_two_nos(10,0)
    #     self.assertRaises(ZeroDivisionError, sample_code1.exception_handler() )

if __name__ == "__main__":
    unittest.main()