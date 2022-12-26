'''Задайте последовательность чисел. Напишите программу, которая выведет список
 неповторяющихся элементов исходной последовательности.'''

#Функция находит повторяющиеся числа в строковом списке и выводит список неповторяющихся элементов исходной последовательности.
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
#Функция находит повторяющиеся числа в числовом списке и выводит список уникальных неповторяющихся элементов исходной последовательности.
def SearchRepeat(lst_int):
    new_lst = []
    [new_lst.append(i) for i in lst_int if i not in new_lst]
    return new_lst

#Программа
list_s = list(input("Введите числа через пробел:\n").split())
list_i=list(map(int, list_s))

#Вывод результата
print(f'Первый вариант решения:{list_i} => {SearchRepeatNumbers(list_s)}')
print(f'Второй вариант решения:{list_i} => {SearchRepeat(list_i)}')


