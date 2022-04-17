res = []
count = 0
max_count = 0
with open('17.txt', 'r') as f:
    for i in range(10000):
        res.append(int(f.readline()))
for i in range(len(res)):
    for y in range(i+1, len(res)):
        if (res[i] + res[y]) % 60 == 0 and (res[i] % 40 == 0 or res[y] % 40 == 0):
            count += 1
            max_count = max(max_count, res[i] + res[y])
print(count, max_count)
