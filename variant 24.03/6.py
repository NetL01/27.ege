for x in range(1, 100):
    for ss in range(0, 100):
        s = 100*ss + x
        n = 1
        while s < 2021:
            s = s + 5*n
            n = n + 1
        if n == 17:
            print('x: ', x, '..s: ', ss)
