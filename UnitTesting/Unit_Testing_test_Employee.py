import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):


    def setUp(self):
        # Создаем объекты класса Employee
        self.emp_1 = Employee('Corey', 'Schafer', 50000)
        self.emp_2 = Employee('Sue', 'Smith', 60000)



    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Sue.Smith@email.com')
# Меняем имя у объекта
        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
# Проверяем, работает ли декоратор property так, чтобы email менялся под изменение имени
        self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
        self.assertEqual(self.emp_2.fullname, 'Sue Smith')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'
        # Проверяем, меняется ли полное имя после изменения основного имени
        self.assertEqual(self.emp_1.fullname, 'John Schafer')
        self.assertEqual(self.emp_2.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()
        # Проверяем, сработал ли метод увеличения зарплаты
        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)



if __name__ == '__main__':
    unittest.main()