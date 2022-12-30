'''Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.'''

from random import randint

'''ФУНКЦИИ'''
#функция создает многочлен
def Polynomial():
    k = randint(1,9)
    list_coeff= [randint(0,100) for i in range(k)] + [randint(1,100)] #создала список коэффициентов из случаных числе от 1 до 100
    str_pomial=' + '.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(list_coeff) if j][::-1]) # создала стоку из коэфициентов и степеней и развернула 
    #str_pomial=str_pomial.replace("**1", "").replace("x**0","")
    #str_pomial += " = 0" 
    string = str_pomial
    return string 

# Функция создает словарь из строки многочлена.
def DisPol(string_pomial):
    dis_pol={}
    string_pomial=string_pomial.replace(" = 0","").replace("+ ","")
    string_pomial=string_pomial.split(" ")
    for i in range(len(string_pomial)):
        string_pomial[i] = string_pomial[i].split("x**")
        dis_pol[int(string_pomial[i][1])] = int(string_pomial[i][0])
    return dis_pol

#Функция спладывает словари и создает из них третий словарь
def Sum_Pol(dis_pol1, dis_pol2):
    sum_pol = {}
    lens = max(max(dis_pol1), max(dis_pol2))
    for i in range (lens, -1, -1):
        dp1=dis_pol1.get(i)
        dp2=dis_pol2.get(i)
        if dp1!=None or dp2!=None:
            sum_pol [i] = (dp1 if dp1 != None else 0) + (dp2 if dp2 != None else 0)
    return sum_pol

#Функция из словаря делает строку многочленов. 
def StrSumPomial (sumPol):
    str_sum_pomial=''
    for i in sumPol.items():
        if str_sum_pomial == '':
            str_sum_pomial+=str(abs(i[1])) + "x**" + str(abs(i[0]))
        else:
            str_sum_pomial+=" + " + str(abs(i[1])) + "x**" + str(abs(i[0])) 
    str_sum_pomial=str_sum_pomial.replace("**1", "").replace("x**0","")
    str_sum_pomial += " = 0" 
    return str_sum_pomial

'''ПРОГРАММА'''
#Записть и чтение из файла file_polynomial1.txt
file_polynomial1 = open("file_polynomial1.txt", "w+")
file_polynomial1.write((Polynomial()))
file_polynomial1 = open("file_polynomial1.txt", "r")
sfp1 = file_polynomial1.read()
#s = (sfp1.replace("**1", "").replace("x**0","")) + ' = 0'
print(f"Многочлен из первого файла: {sfp1}")
file_polynomial1.close()

#Записть и чтение из файла file_polynomial2.txt
file_polynomial2 = open("file_polynomial2.txt", "w+")
file_polynomial2.write((Polynomial()))
file_polynomial2 = open("file_polynomial2.txt", "r")
sfp2=file_polynomial2.read()
#s = (sfp2.replace("**1", "").replace("x**0","")) + ' = 0'
print(f"Многочлен из второго файла: {sfp2}")
file_polynomial2.close()

sumPomial = StrSumPomial((Sum_Pol(DisPol(sfp1), (DisPol(sfp2)))))

#Записть и чтение из файла file_sum_polynomial.txt
file_sum_polynomial = open("file_sum_polynomial.txt", "w+")
file_sum_polynomial.write(f"{sumPomial}")
file_sum_polynomial = open("file_sum_polynomial.txt", "r")
print(f"Сумма многочленов из третьего файла: {file_sum_polynomial.read()}")
file_sum_polynomial.close()