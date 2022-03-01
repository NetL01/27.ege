def func(s):
    n = 740
    while (s + n) < 1200:
        s = s + 6
        n = n - 4
    return n

for i in range(1, 100000):
    if func(i) == 68:
        print(i)

#124
