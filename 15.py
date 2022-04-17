p = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
      28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
q = [23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
     42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58]
max_lenn = 0
lenn = 0
spis_a = []
for a_left in range(0, 100):
    for a_right in range(100, 0, -1):
        if_true = True
        for x in range(0, 100):
            if not(not((x in p) and (x in q)) or ((x in q) and (x in range(a_left, a_right+1)))):
                if_true = False
                # print(a, x)
        if if_true:
            spis_a.append(a_right - a_left)
            print(a_right, a_left)
            #lenn += 1
            #max_lenn = max(max_lenn, lenn)
print(min(spis_a))


#for a in range(0, 100):
#    for x in range(0, 100):
#        if not(((x in p) and (x in q))) or ((x in q) and (x == a)):
#            lenn += 1
#            max_lenn = max(max_lenn, lenn)
#        else:
#            lenn = 0
#print(max_lenn)
