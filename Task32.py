"""Определить индексы элементов массива (списка), значения которых 
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не 
больше заданного максимума)
Ввод:  
[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
5
15
Вывод: [1, 9, 13, 14, 19]"""

numbers = [int(i) for i in input().split()]
low_b, up_b = int(input("Lower border: ")), int(input("Upper border: "))
result = [i for i in range(len(numbers)) if low_b <= numbers[i] <= up_b ]
print(result)
