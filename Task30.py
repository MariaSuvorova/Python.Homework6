"""Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. Формула для 
получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки."""

a1, n = int(input("First element:  ")), int(input("Quantity:  "))
d = int(input("Difference:   "))
arifm = [print(a1+d*i) for i in range(n)]