def func(x):
    a = 1
    b = a
    while a < x:
        c = a + b
        a = b
        b = c
    return b

for i in range(1, 10000):
    if func(i) == 55:
        print(i)

#22
