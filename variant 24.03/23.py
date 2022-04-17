lst = []
def task(start, end):
    if start == end:
        lst.append(1)
        return
    if start > end:
        return
    task(start + 2, end)
    task(start * 3, end)
task(1, 59)
print(sum(lst))
