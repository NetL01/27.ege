import math

lst = []
summ1 = 0
summ2 = 0
max_price = 0
with open('26.txt', 'r') as f:
    for i in range(int(f.readline())):
        lst.append(int(f.readline()))
    lst.sort()
    #
    for i in range(len(lst)):
        if lst[i] <= 50:
            summ2 += lst[i]
        else:
            break
    lst = lst[i:]
    #
    for i in range(len(lst)//2):
        if lst[i] > 50:
            summ1 += lst[i] * 0.75
            max_price = max(max_price, lst[i])
        else:
            summ2 += lst[i]
    for i in range(len(lst)//2, len(lst)):
        summ2 += lst[i]
print(math.ceil(summ1) + summ2, int(max_price))
