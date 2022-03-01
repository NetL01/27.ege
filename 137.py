def func(n):
    s = 350
    while ((2*s) + n) < 1100:
        s = s - 5
        n = n + 15
    return s

for i in range(1, 1000):
    if func(i) == 45:
        print(i)

# 99
