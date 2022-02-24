'''
Имеется набор данных, состоящий из троек положительных целых чисел. Необходимо выбрать из
каждой тройки два числа так, чтобы сумма всех выбранных чисел не делилась на 9 и при этом
была минимально возможной. Гарантируется, что искомую сумму получить можно. Программа
должна напечатать одно число – минимально возможную сумму, соответствующую условиям
задачи.
Входные данные: Даны два входных файла: файл A (27-31a.txt) и файл B (27-31b.txt),
каждый из которых содержит в первой строке количество троек N (1 ≤ N ≤ 100000). Каждая из
следующих N строк содержит три натуральных числа, не превышающих 10 0
Пример входного файла:
6
8 3 4
4 8 12
9 8 11
2 8 3
12 3 5
1 4 11
Для указанных входных данных значением искомой суммы должно быть число 56
В ответе укажите два числа: сначала значение искомой суммы для файла А, затем для файла B.

'''

with open('27-31b.txt', 'r') as f:
    a = int(f.readline())
    res = []
    summ = 0
    max_min = 0
    for i in range(a):
        a, b, c = map(int, f.readline().split())
        summ += max(a, b, c)
        if max_min < min(a, b ,c):
            max_min = min(a, b, c)
        res.append(max(a, b, c))
    if summ % 9 == 0:
        print(summ)
    else:
        res.sort()
        for i in range(len(res)):
            if (summ - res[i] - max_min) % 9 == 0:
                print(summ - res[i] - max_min)
                break