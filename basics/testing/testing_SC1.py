from typing import Any
import unittest
from sample_code1 import divide_two_nos

class DivideNosTestcase(unittest.TestCase):
    """testing sample_code1.py - division of 2 nos"""

    # def __init__(self, methodName: str) -> None:
    #     super().__init__(methodName=methodName)

    def test_normal_nos(self):
        ans = divide_two_nos(10,5)
        self.assertEqual(ans, 2.0)
    
    def test_alphabets(self):
        ans = divide_two_nos('[A-Za-b]','[A-Za-b]')
        self.assertEqual(ans, Any,msg="go home")

if __name__ == "__main__":
    unittest.main()