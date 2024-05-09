import unittest
def city_country(city, country, population=""):
    if population:
        data = f"{city}, {country} - population: {population}"
    else:
        data = f"{city}, {country}"
    return data.title()

class CityCountryTestCase(unittest.TestCase):
    """Test dla programu survey.py"""

    def test_city_country(self):
        location = city_country("santiago", "chile")
        self.assertEqual(location, "Santiago, Chile")

    def test_city_country_population(self):
        location = city_country("santiago", "chile", 6269384)
        self.assertEqual(location, "Santiago, Chile - Population: 6269384")

if __name__ == "__main__":
    unittest.main()