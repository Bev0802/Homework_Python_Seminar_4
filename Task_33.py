'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

from random import randint
##Функция создадние многочлена
def Pomial(c):
    list_coeff=[]
    for i in range(c+1):
        list_coeff.append(randint(0,100))
    str_pomial=''
    for i, j in enumerate(list_coeff):
            if k==i:
                str_pomial=str_pomial + f"{(j,'')[j==0]}x**{i}"
            else:
                str_pomial=str_pomial + f"{(j,'')[j==0]}x**{i}+"
          
    lst_pomial = list(str_pomial.split("+"))
    str_pomial = ' + '.join(x for x in lst_pomial[::-1])
    str_pomial = str_pomial.replace('**1','').replace('x**0', '') + ' = 0'
    return str_pomial    
# end def


k = int(input("Введите число натульной степени: "))

list_coeff= [randint(0,100) for i in range(k)] + [randint(1,100)] #создала список коэффициентов из случаных числе от 1 до 100
str_pomial=' + '.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(list_coeff) if j][::-1]) # создала стоку из коэфициентов и степеней и развернула 

#Убала лишние символы и добавила равенстов.
str_pomial=str_pomial.replace("**1", "").replace("x**0","") + " = 0"

#Вывод на печать
print(f"Создали многочлен: k={k} = > {str_pomial}")
print(f"Создали многочлен(второй вариант): k={k} = > {Pomial(k)}")

#Записть и чтение из файла
file_polynomial = open("file_polynomial.txt", "w+")
file_polynomial.write((f"k={k} = > {str_pomial}"))
file_polynomial = open("file_polynomial.txt", "r")
print(f"Прочитали из файла записанный туда многочлен: {file_polynomial.read()}")
file_polynomial.close()