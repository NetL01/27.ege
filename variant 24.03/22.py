for y in range(0, 1000):
    q = 0
    n = y
    for i in range(1, n):
        if n % i == 0:
            q = i
    if q == 17:
        print(y)
