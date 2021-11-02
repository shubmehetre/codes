import unittest
import city_func

class CityTest(unittest.TestCase):
    def test_normal_input(self):
        ans = city_func.city_country("Pune","india")
        self.assertEqual(ans, "Pune, India")
    def test_for_pop(self):
        ans = city_func.city_country("Pune","india",5000)
        self.assertEqual(ans, "Pune, India, Population = 5000")

if __name__ == "__main__":
    unittest.main()

