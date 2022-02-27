with open('27-B_1.txt', 'r') as f:
    rounds = int(f.readline())
    summ = 0
    min_diff = 0
    for i in range(rounds):
        one, two = map(int, f.readline().split())
        a = max(one, two)
        summ += a
        if abs(one - two) % 5 == 0:
            min_diff = abs(one - two)
    if summ % 5 == 0:
        print(summ-min_diff)
    else:
        print(summ)
    
        
        

