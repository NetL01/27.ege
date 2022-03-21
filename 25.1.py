for i in range(123456789, 223456789 + 1):
    count = 0
    t = i**0.5
    if t == int(t):
        count += 1
        divider = 0
        for j in range(2, int(t)):
            if i % j == 0:
                count += 2
                divider = i // j
            if count > 3:
                break
        if count == 3:
            print(i, divider)
            
        
