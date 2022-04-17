res = []
max_summ = 0
count = 0
with open('26.txt', 'r') as f:
    a = int(f.readline())
    for i in range(a):
        res.append(int(f.readline()))
    for i in range(len(res)):
        for y in range(i+1, len(res)):
            b = res[i] + res[y]
            if b % 2 != 0 and b in res:
                max_summ = max(max_summ, b)
                count += 1
print(max_summ, count)
