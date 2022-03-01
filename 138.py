def func(s):
    n = 600
    while n > s:
        s = s + 3
        n = n - 6
    return n

for i in range(1, 1000):
    if func(i) == 210:
        print(i)

#1523
