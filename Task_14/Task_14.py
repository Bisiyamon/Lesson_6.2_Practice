#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите предельное число N: "))
i = 1
degree = 2**i
while degree <= N:
    degree = 2**i
    if degree < N:
        print(i, degree)
        i += 1
    else:
        print("Финал")

