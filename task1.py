# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.


my_list = [1, 1, 3, 4, 4, 3, 2, 5, 6]
print(*filter(lambda i: my_list.count(i) == 1, my_list))