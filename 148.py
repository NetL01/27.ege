def func(x):
    s = 6 * (x // 15)
    n = 1
    while s < 300:
        s = s + 18
        n = n * 2
    return n
count = 0
for i in range(1, 10000):
    if func(i) >= 2 and func(i) <= 500:
        count += 1
print(count)
#360
