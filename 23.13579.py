lst = []

def task(start, stop):
    if start == stop:
        lst.append(1)
        return
    if start > stop:
        return
    task(start + 1, stop)
    if start != 7:
        task(start + 2, stop)
    if start != 5 and start != 6 and start != 7:
        task(start + 4, stop)
    
    

task(1, 15)
print(sum(lst))
