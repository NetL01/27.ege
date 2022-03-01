def func(x):
    while x < 100:
        if (x % 2) < 1:
            x = x // 2
        else:
            x = (3 * x) + 1
    print(x)

for i in range(0, 100):
    func(i)

#0

