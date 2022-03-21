st = '''Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m».

Для какого наибольшего натурального числа А формула

(A < 50) ∧ (¬ДЕЛ(x, А) → (ДЕЛ(x, 10) → ¬ДЕЛ(x, 12)))

тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной x)?

Спрятать решение
Решение.
Рассмотрим такие x, при которых скобка (ДЕЛ(x, 10) → ¬ДЕЛ(x, 12)) будет ложной. Это x, которые делятся без остатка одновременно на 10 и на 12. Наименьшее общее кратное этих чисел равно 60.

Следовательно, для х = 60 выражение ¬ДЕЛ(x, А) должно быть ложным, то есть число 60 должно делиться на А < 50. Наибольшим таким А является число 30. Это и будет ответ.

 

Ответ: 30.'''


for a in range(1, 100):
    bools = True
    for x in range(1, 100):
        if not (a < 50 and (not((x % a) == 0) <= (((x % 10) == 0) <= (not(x % 12 == 0))))):
            bools = False
    if bools:
        print(a)
    bools = True
