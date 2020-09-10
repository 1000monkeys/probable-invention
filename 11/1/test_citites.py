import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """tests for city_functions.py"""

    def test_city_country(self):
        """Does it output according to expectations?"""
        output = city_country("groningen", "nederland")
        self.assertEqual(output, "Groningen, Nederland")

        output = city_country("santiago", "chile")
        self.assertEqual(output, "Santiago, Chile")