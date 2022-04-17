lst = []
max_diff = 0
count = 0
with open('17.txt', 'r') as f:
    for i in range(10000):
        lst.append(int(f.readline()))
    for i in range(len(lst)):
        for y in range(i+1, len(lst)):
            if abs(lst[i] - lst[y]) % 80 == 0:
                count += 1
                max_diff = max(max_diff, abs(lst[i] - lst[y]))
print(count, max_diff)
        
