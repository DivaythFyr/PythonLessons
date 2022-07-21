class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        return self.a + self.b + self.c

class B(A):
    def __init__(self, a2, b2, c2):
        super().__init__(a2, b2, c2)


    def Sum(self):
        return 6

ObjectB = B(2, 3, 4)
#print(ObjectB.sum())
#print(ObjectB.Sum())





class NumberStringSegregator:
    def __init__(self, num_str_list):
        self.num_str_list = num_str_list

    def AppendNumStrFromList(self):
        List_str = []
        List_num = []

        for i, element in enumerate(self.num_str_list):
            if type(element) == int:
                List_num.append(element)
            else:
                List_str.append(element)

        return List_num, List_str

class fgfg(NumberStringSegregator):
    def __init__(self, List):
        super().__init__(List) # здесь нужно задать такое же количество аргументов, как и в init родителя
        self.List_num, self.List_str = super().AppendNumStrFromList() # это метод родителя, он возвращает два списка
        #print(self.List_num, self.List_str)
#FG = fgfg([1, 2, 3, 'fgf'])
#print(FG)

# Домашняя Задача: Класс наследует от этого класса. Он должен взять списки чисел и строк.
# Список строк просто распечатываем
# Список чисел меняем - каждое значение увеличиваем на единицу
# self.List_num, self.List_str = super().AppendNumStrFromList





