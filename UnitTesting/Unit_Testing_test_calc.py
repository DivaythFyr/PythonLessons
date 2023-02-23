import unittest
import calc

class TestCalc(unittest.TestCase):

# Все тесты должны начинаться со слова test_
    def test_add(self):
        # Так как unittest построен на классах,
        # использование его методов требует self
        self.assertEqual(calc.add(10, 5), 15)



    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        
        with self.assertRaises(ValueError):
            calc.divide(10, 0)


    # # если мы просто активируем тест с помощью: python название файла.py
# # то ничего не произойдет
# # Нужно пользоваться python -m unittest название файла.py
# # python -m unittest Unit_Testing_test_calc.py

# Задание: добавить в функцию test_add assertEqual для сложения отрицательного и положительного
# и сложения двух отрицательных (любые числа)

# Задание: добавить такие же функции в этот класс для вычитания, умножения, деления

# Задание: Добавить тест в функцию деления, который проверяет, что
# не происходит деления на ноль self.assertRaises(ValueError, calc.divide, 10, 0)




if __name__ == '__main__':
    unittest.main()



