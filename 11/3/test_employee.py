import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    

    def setUp(self):
        self.employee = Employee("Kjell", "Vos", "1000000")

    def test_give_default_raise(self):
        salary_before = self.employee.salary
        self.employee.get_raise()
        salary_after = self.employee.salary
        self.assertEqual(int(salary_before) + 5000, salary_after)

    def test_give_custom_raise(self):
        salary_before = self.employee.salary
        self.employee.get_raise(25000)
        salary_after = self.employee.salary
        self.assertEqual(int(salary_before) + 25000, salary_after)
