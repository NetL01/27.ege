for i in range(185311, 185331):
    if i**0.5 != int(i**0.5):
        #print(i)
        dels = []
        for y in range(1, int(i**0.5)+1):
            if i % y == 0:
                dels.append(y)
                dels.append(int(i/y))
        if len(dels) == 4:
            print(i, dels)
        
#def task(num):
#    dels1 = []
#    for y in range(2, int(num**0.8)):
#        if num % y == 0:
#            dels1.append(y)
#    print(num, dels1)

#task(185314)
#task(185321)
#task(185329)
