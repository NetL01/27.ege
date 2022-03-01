def func(x):
    s = 7 * (x // 8)
    n = 1
    while s < 300:
        s = s + 18
        n = n * 3
    return n
count = 0
for i in range(1, 10000):
    if func(i) == 81:
        count += 1
print(count)
#24
