'''Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.'''

from random import randint
def Polynomial():
    k = randint(1,9)
    list_coeff= [randint(0,100) for i in range(k)] + [randint(1,100)] #создала список коэффициентов из случаных числе от 1 до 100
    str_pomial=' + '.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(list_coeff) if j][::-1]) # создала стоку из коэфициентов и степеней и развернула 
    str_pomial=str_pomial.replace("**1", "") 
    str_pomial=str_pomial.replace("x**0","")
    str_pomial += " = 0" 
    string = f"k={k} = > {str_pomial}"
    return string 

#Записть и чтение из файла
file_polynomial = open("file_polynomial.txt", "w+")
file_polynomial.write((Polynomial()))
file_polynomial = open("file_polynomial.txt", "r")
print(sfp:=f"Многочлен из первого файла: {file_polynomial.read()}")
file_polynomial.close()

file_polynomial1 = open("file_polynomial1.txt", "w+")
file_polynomial1.write((Polynomial()))
file_polynomial1 = open("file_polynomial1.txt", "r")
print(sfp1:=f"Многочлен из второго файла: {file_polynomial1.read()}")
file_polynomial1.close()

sfp=sfp.replace(" 0","")
sfp=sfp[36:]
sfp1=sfp1.replace(" = 0", "")
sfp1=sfp1[36:]

file_sum_polynomial = open("file_sum_polynomial.txt", "w+")
file_sum_polynomial.write(f"{sfp} {sfp1}")
file_sum_polynomial = open("file_sum_polynomial.txt", "r")
print(f"Сумма многочленов из третьего файла: {file_sum_polynomial.read()}")
file_sum_polynomial.close()
