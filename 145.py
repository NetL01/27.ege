def func(x):
    s = 5 * (x // 10)
    n = 1
    while s < 300:
        s = s + 28
        n = n * 3
    return n
count = 0
for i in range(0,10000):
    if func(i) == 243:
        count += 1
#0
