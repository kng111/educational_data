# Задание 1: Сравнение Эффективности Циклов

# 1.1. Задача для Оптимизации:

# Ваша задача - написать наиболее эффективный цикл для нахождения суммы квадратов чисел от 1 до N,
#  где N - положительное целое число. 
# Предложите несколько вариантов циклов и определите наилучший с точки зрения производительности.

# 1.2. Пример для Замедления:

# Напишите медленный вариант цикла для той же задачи (нахождение суммы квадратов чисел от 1 до N).
#  Используйте неоптимальный подход к решению и объясните, 
# почему этот вариант менее эффективен.

# Задание 2: Оценка Скорости Работы Строковых Методов

# 2.1. Задача для Оптимизации:

# Напишите код для конкатенации списка строк в единую строку. 
# Затем предложите наиболее эффективный способ выполнения этой задачи.

# 2.2. Пример для Замедления:

# Реализуйте медленный вариант конкатенации списка строк. Используйте неоптимальные методы для соединения строк и объясните, 
# почему такой подход может быть медленным.

# Эти задания помогут вам оценить эффективность различных подходов к написанию кода и понять,
#  какие методы могут привести к более быстрой или медленной работе программы.








# 1.1. Задача для Оптимизации:
# import time

# def optimal_sum_of_squares(N):
#     return sum(i**2 for i in range(1, N+1))

# # Измерение времени выполнения
# start_time = time.time()
# result = optimal_sum_of_squares(100_000)
# end_time = time.time()

# print(f"Оптимальный результат: {result}")
# print(f"Время выполнения: {end_time - start_time} секунд")



# 1.2. Пример для Замедления:

# import time

# def slow_sum_of_squares(N):
#     result = 0
#     for i in range(1, N+1):
#         result = result + i**2  # Используем неоптимальный способ
#     return result

# # Измерение времени выполнения
# start_time_slow = time.time()
# result_slow = slow_sum_of_squares(100_100_100)
# end_time_slow = time.time()

# print(f"Медленный результат: {result_slow}")
# print(f"Время выполнения: {end_time_slow - start_time_slow} секунд")


# 2.1. Задача для Оптимизации:
# import time

# def slow_sum_of_squares(N):
#     result = 0
#     i = 1
#     while i <= N:
#         result = result + i**2  # Медленный вариант с задержкой
#         i += 1
#     return result

# # Измерение времени выполнения
# start_time_slow = time.time()
# result_slow = slow_sum_of_squares(100_100_100)
# end_time_slow = time.time()

# print(f"Медленный результат: {result_slow}")
# print(f"Время выполнения: {end_time_slow - start_time_slow} секунд")




