# import timeit
# import numpy as np

# value = 100_100_100

# def loop1() -> int:
#     return sum(range(value))

# # Функция zxc1 теперь возвращает сумму четных чисел и сумму квадратов чисел.
# def zxc1():

#     squared_numbers = sum(x * 2 for x in range(1, value))  # Используем значение переменной value вместо жестко заданного предела.
#     return squared_numbers

# # Функция zxc2 теперь также возвращает сумму удвоенных элементов массива NumPy.
# def zxc2():
    
#     result = np.sum(range(value))
#     return result




# print(f"zxc1: {timeit.timeit(zxc1, number=1)}")
# print(f"zxc2: {timeit.timeit(zxc2, number=1)}")


# from collections import namedtuple

# ntuple = namedtuple('ntuple',['x','y'])
# n = ntuple(1,2)

# if isinstance(n,ntuple):
#     print('tuple')

# import hashlib

# match "hello world":
#     case "hello world" as f:
#         print(hashlib.sha256(f.encode()).hexdigest())


# import time

# def xx():
#     squared_numbers = sum(x**2 for x in range(1, 240_500_100))
#     return squared_numbers

# def measure_execution_time(func):
#     start_time = time.time()
#     result = func()
#     end_time = time.time()
#     return result, start_time, end_time

# result, start_time, end_time = measure_execution_time(xx)

# print(f"Result: {result}")
# print(f"Time: {end_time - start_time} seconds")

# print(4_636_865_796_773_922_657_078_350 / 60)
# 772810970000000000_000_000_000_000
# print(77281097 * 10**22)

# def loop1() -> int:
#     return sum(range(value))





# for i in range(len(x)):
#     print(x[i])

# word = 'Подпишись'
# letter_count = {}

# for letter in word:
#     letter_count[letter] = letter_count.get(letter, 0) + 1

# result = [(key, value) for key, value in letter_count.items()]
# print(result)



# slovo = 'Подпишись'

# def slovakey(slovo):
#     list1 = []
#     for i in range(len(slovo)):
#         list1.append(slovo[i])
#     return list1

# def count_letters(slovo):
#     letter_count = {}
#     for letter in slovo:
#         letter_count[letter] = letter_count.get(letter, 0) + 1
#     return letter_count

# slovo_list = slovakey(slovo)
# letter_count = count_letters(slovo_list)

# for key, value in letter_count.items():
#     print(f"{key}: {value}")
# list1 = []
# for i in range(2):
#     try:
        
#         list1.append(input())
#     except:
#         break

# for i in range(len(list1)):
#     print(int(list1[1]) * 365) -  (int(list1[0]) * 365)

# def count_days_between_years(year1, year2):
#     days = 0
#     for year in range(min(year1, year2), max(year1, year2)):  # Включаем последний год
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             days += 366  # Високосный год
#         else:
#             days += 365  # Невисокосный год
#     return days

# # Ввод данных
# year1 = int(input())
# year2 = int(input())

# # Вывод результата
# print(count_days_between_years(year1, year2))

# import timeit
# value = 100_100_100
# def for1():
#     list1 = []
#     for i in range(value):
#         list1.append(i ** 2)
#     return sum(list1)
# print(timeit.timeit(for1, number=1))
# print(for1())
# import os
# os.system("pause")

import timeit
import numpy
def loop1() -> int:
        values = numpy.arange(1, 100_100_100_0)
        result = numpy.sum(values ** 2)
        return result
print(f"zxc1: {(timeit.timeit(loop1, number=1))}")
print(loop1())
import os
os.system("pause")