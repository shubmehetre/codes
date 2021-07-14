import unittest
import sample_code1

class AddNosTest(unittest.TestCase):
    """testing sample_code1.py - add of nos"""

    # def __init__(self, methodName: str) -> None:
    #     super().__init__(methodName=methodName)

    def test_normal_nos(self):
        ans = sample_code1.add_nos(10,5)
        self.assertEqual(ans, 15.0)

    def test_three_nos(self):
        ans = sample_code1.add_nos(100, 50, 0)
        self.assertEqual(ans, 150.0)

if __name__ == "__main__":
    unittest.main()
