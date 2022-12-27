'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

from random import randint
k = int(input("Введите число натульной степени: "))

list_coeff= [randint(0,100) for i in range(k)] + [randint(1,100)] #создала список коэффициентов из случаных числе от 1 до 100
str_pomial=' + '.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(list_coeff) if j][::-1]) # создала стоку из коэфициентов и степеней и развернула 

#Убала лишние символы и добавила равенстов.
str_pomial=str_pomial.replace("**1", "") 
str_pomial=str_pomial.replace("x**0","")
str_pomial += " = 0" 

#Вывод на печать
print(f"Создали многочлен: k={k} = > {str_pomial}")

#Записть и чтение из файла
file_polynomial = open("file_polynomial.txt", "w+")
file_polynomial.write((f"k={k} = > {str_pomial}"))
file_polynomial = open("file_polynomial.txt", "r")
print(f"Прочитали из файла многочлен: {file_polynomial.read()}")
file_polynomial.close()    