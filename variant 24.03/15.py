for a in range(0, 100):
    fl = True
    for x in range(0, 100):
        if not(x&41 == 0 or x&33!=0 or x&a != 0):
            fl = False
        if fl == False:
            break
    if fl:
        print(a)
