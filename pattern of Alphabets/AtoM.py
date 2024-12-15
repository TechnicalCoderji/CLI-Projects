#dipparmar
list2 = []
symbol = "#"
#AtoZ
#A
print_A = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and col!=0 and col!=4):
            print_A[row][col] = symbol
list2.append(print_A)

#B
print_B = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((row==0 or row==3 or row==6) and col!=4) or ((col==0 or col==4) and row!=0 and row!=3 and row!=6):
            print_B[row][col] = symbol
list2.append(print_B)

#C
print_C = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if (col==0 and row!=0 and row!=6) or ((row==0 or row==6) and col!=0):
            print_C[row][col] = symbol
list2.append(print_C)

#D
print_D = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==6) and col<4) or (col==4 and (row>0 and row<6)):
            print_D[row][col] = symbol
list2.append(print_D)

#E
print_E = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3 or row==6) and col!=5):
            print_E[row][col] = symbol
list2.append(print_E)

#F
print_F = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if (col==0) or ((row==0 or row==3) and col!=5):
            print_F[row][col] = symbol
list2.append(print_F)

#G
print_G = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or row==0 or row==6 or (row==3 and col>1) or (col==4 and row>2):
            print_G[row][col] = symbol
list2.append(print_G)

#H
print_H = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or row==3:
            print_H[row][col] = symbol
list2.append(print_H)

#I
print_I = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if row==0 or row==6 or col==2:
            print_I[row][col] = symbol
list2.append(print_I)

#J
print_J = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if row==0 or (row==6 and col<3) or col==2:
            print_J[row][col] = symbol
list2.append(print_J)

#K
print_K = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or row+col==4 or row-col==2:
            print_K[row][col] = symbol
list2.append(print_K)

#L
print_L = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if row==6 or col==0:
            print_L[row][col] = symbol
list2.append(print_L)

#M
print_M = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row<3 and (col==row or col+row==4)):
            print_M[row][col] = symbol
list2.append(print_M)

#dipparmar for printing
for i in range(7):
    for j in range(len(list2)):
        for k in range(5):
            print(list2[j][i][k],end=" ")
        print(end=" ")
    print()