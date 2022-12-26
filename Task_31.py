'''Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
Простое число - это число, которое без осткатка, делится только на само себя и на единицу.'''

n=int(input('Введите целое положительное число: '))

def ListPrimeFactorsNumber(num):
    list_mul = []
    i=2
    n=num
    while i*i<=num:
        while num % i==0:
                list_mul.append(i)
                num = num / i
        i = i + 1
    if num > 1:
            list_mul.append(int(num))
    if num == n:
        print (f"У числа {n} нет простых множителей, т.к. оно само является простым числом.")
        quit()
    return list_mul


print (n, ' => ', ListPrimeFactorsNumber(n))
