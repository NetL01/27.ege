for a in range(1, 101):
    count = 0
    for x in range(1, 101):
        if (x // a == 0) or (not((x // 6 == 0) and (x // 9 == 0))):
            count += 1
    if count == 100:
        print(a)
                         
                     
