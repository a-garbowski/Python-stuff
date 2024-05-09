import unittest
from diy import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the Employee class."""

    def setUp(self):
        self.worker = Employee("Adam", "Nowak", 60000)

    def test_give_default_raise(self):
        self.initial_salary = self.worker.yearly_salary
        self.worker.give_raise()
        self.assertEqual(self.worker.yearly_salary, self.initial_salary + 5000)

    def test_give_custom_raise(self):
        self.initial_salary = self.worker.yearly_salary
        self.worker.give_raise(8000)
        self.assertEqual(self.worker.yearly_salary, self.initial_salary + 8000)

