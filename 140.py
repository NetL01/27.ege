def func(s):
    n = 10
    while (s - n < 1000):
        s = s + n
        n = n + 5
    return n

count = 0
for i in range(1,100000):
    if func(i) == 80:
        count += 1
print(count)
#70
