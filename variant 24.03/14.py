def func(num, base):
    newnum = ''
    while num > 0:
        newnum = str(num%base) + newnum
        num //= base
    return newnum
        


for i in range(0, 100):
    if i%11 == 1:
        print('i: ', i, 'base6: ', func(i, 6), 'base5: ', func(i, 5))
        
        
