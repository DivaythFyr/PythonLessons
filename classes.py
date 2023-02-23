
class node:
    def __init__(self,data=None): # data - значение узла
        self.data=data
        self.next=None # здесь хранится референс на следующий

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node


# Показывает элементы связанного списка в виде обычного списка
    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


# Возвращает длину связанного списка
    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total

# Возвращает значение по индексу
    def get(self, index):
        if index >= self.length() or index < 0:
            print('Индекс вне диапазона')
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node=cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx+=1