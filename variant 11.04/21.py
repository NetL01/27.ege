def move(k1,k2):
    return (k1+1,k2), (k1,k2+1), (k1*2,k2), (k1, k2*3)

def win(k1,k2):
    return k1+k2 >=69

buff = [[0]*210 for i in range(210)]

for i in range(0, 70):
    for j in range(0,70):
        if any(win(k1,k2) for k1,k2 in move(i,j)):
            buff[i][j] = 1

for i in range(0, 70):
    for j in range(0,70):
        if buff[i][j] ==0 and all(buff[k1][k2]==1 for k1,k2 in move(i,j)):
            buff[i][j] = -1

##for i in range(0, 70):
##    for j in range(0,70):
##        if buff[i][j] == 0 and any(buff[k1][k2]==-1 for k1,k2 in move(i,j)):
##            buff[i][j] = 2       
##
##for i in range(0, 70):
##    for j in range(0,70):
##        if buff[i][j] == 0 and all(buff[k1][k2]>0 for k1,k2 in move(i,j)):
##            buff[i][j] = -2       


print(*enumerate(buff[10][:100]), sep="\n")
