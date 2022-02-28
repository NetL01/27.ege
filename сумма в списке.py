with open('27a.txt', 'r') as f:
    res = list(map(int, f.readline().split()))
    k = res[0]
    check = []
    for i in range(1, len(res)):
        if (k - res[i]) in check:
            print(k - res[i], res[i])
            break
        else:
            check.append(res[i])
