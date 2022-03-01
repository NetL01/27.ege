def func(x):
    s = 6 * (x // 5)
    n = 1
    while s < 300:
        s = s + 35
        n = n * 2
    return n
count = 0
for i in range(1, 10000):
    if func(i) == 64:
        count += 1
print(count)
#30
