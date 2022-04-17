with open('24.txt', 'r') as f:
    a = f.readline()
    max_count = 0
    count = 0
    for i in range(len(a)):
        if a[i] == "L":
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0
print(max_count)
    
