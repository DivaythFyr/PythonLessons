# Unit test - встроенный модуль для тестирования кода,
# дает значительно больший функционал для тестирования и предотвращения ошибок,
# чем голое использование try except

# TestCase - класс, который предоставляет наиболее часто встречаемые assert.
# Method                                    Checks that
# assertEqual(a, b)                            a == b
# assertNotEqual(a, b)                         a != b
# assertTrue(x)                                bool(x) is True
# assertFalse(x)                               bool(x) is False
# assertIn(a, b)                               a in b

# unittest имеет базовые assert для проверки обработки исключений
# Method                                    Checks that
# assertRaises(exc, fun, *args, **kwds)     fun(*args, **kwds) raises exc
# assertWarns(warn, fun, *args, **kwds)     fun(*args, **kwds) raises warn
# и так далее
#

# Unittesting mock
