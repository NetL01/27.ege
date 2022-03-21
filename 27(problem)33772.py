# четный min_diff
min_diff_even = -1

# нечётный min_diff
min_diff_odd = -1
count = 0
with open('27_a.txt', 'r') as f:
    rounds = int(f.readline())
    for i in range(rounds):
        a, b = list(map(int, f.readline()))
        count += min(a, b)
        if min(a, b) % 2 == 0:
            min_diff_even = min(min_diff_even, min(a, b))
        if min(a, b) % 2 != 0:
            min_diff_odd = min(min_diff_odd, min(a, b))
                            
        
        
        
