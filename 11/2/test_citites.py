import unittest
from city_functions import city_country_population

class TestCityCountry(unittest.TestCase):
    """tests for city_functions.py"""

    def test_city_country(self):
        """Does it output according to expectations?"""
        output = city_country_population("groningen", "nederland")
        self.assertEqual(output, "Groningen, Nederland")

        output = city_country_population("santiago", "chile")
        self.assertEqual(output, "Santiago, Chile")

    def test_city_country_population(self):
        """Does the optional parameter wreck things?"""
        output = city_country_population("groningen", "nederland", "150000")
        self.assertEqual(output, "Groningen, Nederland - population 150000")
