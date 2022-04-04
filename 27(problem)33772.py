# четный min_diff
min_diff_even = []

# нечётный min_diff
min_diff_odd = []
count = 0
count_even = 0
count_odd = 0
with open('27_a.txt', 'r') as f:
    rounds = int(f.readline())
    for i in range(rounds):
        a, b = list(map(int, f.readline()))
        
        if min(a, b) % 2 == 0:
            min_diff_even.append(min(a, b))
            count += min(a, b)
            count_even += 1
        if min(a, b) % 2 != 0:
            min_diff_odd.append(min(a, b))
            count += min(a, b)
            count_odd += 1
    if count_even > count_odd and count % 2 == 0:
        print(count)
    if count_even > count_odd and count % 2 != 0:
        print(count)
        
                            
        
        
        
