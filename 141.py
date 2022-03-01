def func(s):
    n = 1
    while s > n:
        s = s - 15
        n = n * 5
    return n

count = 0
for i in range(1,100000):
    if func(i) == 125:
        count += 1
print(count)
#115
