s = int(input())
x = int(input())
s = 100*s + x
n = 1
while s < 2021:
    s = s + 5*n
    n = n + 1
print(n)
