'''Задайте последовательность чисел. Напишите программу, которая выведет список
 неповторяющихся элементов исходной последовательности.'''
# ФУНКЦИИ
# Функция находит повторяющиеся числа в строковом списке и выводит список неповторяющихся элементов.
def SearchRepeatNumbers(list_string):
    new_lst = []
    i = 0
    while i < len(list_string):
        l = list_string[i]
        if (list_string.count(l)) == 1:
            new_lst.append(l)
        i = i+1
    list_int = list(map(int, new_lst))
    return list_int

# Функция находит повторяющиеся числа в числовом списке и выводит список уникальных неповторяющихся элементов исходной последовательности.
def SearchRepeat(lst_int):
    new_lst = []
    [new_lst.append(i) for i in lst_int if i not in new_lst]
    return new_lst

# ВВОД ДАННЫХ
list_s = list(input("Введите числа через пробел:\n").split())
list_i = list(map(int, list_s))

# ВЫВОД РЕЗУЛЬТАТА
print(f'Первый вариант решения:{list_i} => {SearchRepeatNumbers(list_s)}')
print(f'Второй вариант решения:{list_i} => {SearchRepeat(list_i)}')