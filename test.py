import unittest
from gfn import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Testy dla programu 'exercise.py'"""

    def test_first_last_name(self):
        """Czy dane w postaci 'Karol Strasburger' są osbługiwane prawidłowo?"""
        formatted_name = get_formatted_name("Karol", "Strasburger")
        self.assertEqual(formatted_name, "Karol Strasburger")

    def test_first_last_middle_name(self):
        """Czy dane w postaci 'Wolfgang Amadeus Mozart' są obsługiwane prawidłowo?"""
        formatted_name = get_formatted_name("wolfgang", "mozart", "amadeus")
        self.assertEqual(formatted_name, "Wolfgang Amadeus Mozart")

if __name__ == "__main__":
    unittest.main()