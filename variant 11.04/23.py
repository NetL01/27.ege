lst = []
def task(start, end):
    if start == end:
        lst.append(1)
        return
    if start > end:
        return
    task(start + 1, end)
    task(start * 2, end)
task(2, 22)
print(sum(lst))
