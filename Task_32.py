'''Задайте последовательность чисел. Напишите программу, которая выведет список
 неповторяющихся элементов исходной последовательности.'''

#Функция находит повторяющиеся числа и выводит список неповторяющихся элементов исходной последовательности.
def SearchRepeatNumbers(list_string):
    lens = len(list_string)
    i=0
    k=1
    while i<lens-1:
        l = list_string[i]
        while k<lens-1:
         k=k+1
         if l==list_string[k]:
             m=list_string[k]
             list_string.remove(m)
             list_string.remove(l)
             lens=len(list_string)
             break
        i=i+1
        k=i
    list_int=list(map(int, list_string))
    return list_int

list_s = list(input("Введите числа через пробел:\n").split())
list_i=list(map(int, list_s))

print(f'{list_i} => {SearchRepeatNumbers(list_s)}')


