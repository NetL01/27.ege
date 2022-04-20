lst = []

def task_23(start, stop):
    if start == stop:
        lst.append(1)
        return
    if start > stop:
        return
    task_23(start + 1, stop)
    if start != 7:
        task_23(start + 2, stop)
    if start < 3:
        task_23(start * 3, stop)


task_23(1,15)
print(sum(lst))
