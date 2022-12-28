# Сложность измеряется не в конкретных величинах
# А в нарастании сложности. f(n). O(n)

# f(n) = c  Постоянная сложность (функция-константа)
# Вне зависимости от размера данных совершает
# всегда одно и тоже количество действий
[].append(1000)
2 < 4

# Линейная сложность f(n) = n
max([10, 20, 30, 40, 50])

# Линейно-логарифмическая f(n) = nlogn
# Сортировка слиянием, быстрая сортировка

# Квадратическая f(n) = n^2

# Кубическая

# Экспоненциальная f(n) = b^n

# f(n) = n!logn  алгоритм Комивояжера  8 городов



# Логарифмеческая сложность  f(n) = log n
# бинарный поиск
def binary_search(item, list):
    low = 0  # индекс левой границы
    high = len(list) - 1  # индекс правой границы
#    [1, 4, 44, 55, 68, 77, 100]
    while low <= high:
        mid = (low + high) // 2 # на каждом обороте цикла будет инициализироваться
        # порядковый номер среднего элемента
        guess = list[mid] # и сам средний элемент относительно этого порядкового номера

        if guess == item:
            return mid
        if item < guess: # если элемент меньше того,
            # что посередине
            high = mid - 1 # то самой
            # верхней границей становится элемент до среднего
        else:
            low = mid + 1
    return None # элемента нет в списке
print(binary_search(2, [1, 2, 4, 6, 7, 8, 9]))



# сортировка выбором
def findSmallest(arr): # принимает список
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
#print(findSmallest([3, 2, 1]))

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest)) # добавляем этот элемент
        # в новый список
        # и удаляем из старого
    return newArr
#print(selectionSort([1, 2, 2, 4, 4, 4, 3, 3]))


def FindValueInUnsorted(item, *args):
    num_list = [*args]

    sorted_num_list = selectionSort(num_list)

    return binary_search(item, sorted_num_list)

#print(FindValueInUnsorted(2, 1, 3, 4, 2))



def CorrectFib(n):
    a = 0
    b = 1

    if n <= 2:
        return 1
    else: # 1, 1, 2, 3, 5, 8, 13, 24
        for i in range(1, n): # n = 4
            c = a + b # 1  ->  2  ->  3
            a = b     # 1  ->  1  ->  2
            b = c     # 1  ->  2  ->  3
    return b

def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
    return (a+b, a)
#print(good_fibonacci(5))


# Задание: сортировку выбором, но обратную. По убыванию

# Функция принимает бесконечное количество чисел
# Нужно бинарным поиском найти число по позиции, которую хочет пользователь
# *args

def AA():
    return 2 + 2

def AAA():
    x = AA()
    return 2


# Сортировка вставкой
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1

        # Place key at after the element just smaller than it.
        array[j + 1] = key




# Сортировка слиянием
def merge(left, right):
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left

    result = []
    index_left = index_right = 0
    while len(result) < len(left) + len(right):
        if left[index_left] <= right[index_right]:
            result.append(left[index_left])
            index_left += 1
        else:
            result.append(right[index_right])
            index_right += 1

        if index_right == len(right):
            result += left[index_left:]
            break

        if index_left == len(left):
            result += right[index_right:]
            break
    return result


def merge_sort(array):
    # If the input array contains fewer than two elements,
    # then return it as the result of the function
    if len(array) < 2:
        return array

    midpoint = len(array) // 2

    # Sort the array by recursively splitting the input
    # into two equal halves, sorting each half and merging them
    # together into the final result
    return merge(
        left=merge_sort(array[:midpoint]),
        right=merge_sort(array[midpoint:]))