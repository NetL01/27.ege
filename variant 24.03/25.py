for i in range(289123456, 389123456 + 1):
    if i**0.5 == int(i**0.5):
        dels1 = []
        for y in range(2, int(i**0.8)):
            if i % y == 0:
                dels1.append(y)
        if len(dels1) == 3:
            print(i, max(dels1))
