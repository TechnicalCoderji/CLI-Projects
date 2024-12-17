#dipparmar
list2 = []
symbol = input("Enter Any Symbol: ")
#AtoZ
#N
print_N = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (row<2 and col==1) or (col==2 and row>1 and row<4) or (col==3 and row>3 and row<6):
            print_N[row][col] = symbol
list2.append(print_N)

#O
print_O = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0 and row!=6) or ((row==0 or row==6) and col!=0 and col!=4):
            print_O[row][col] = symbol
list2.append(print_O)

#P
print_P = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3) and col!=4) or (col==4 and row!=0 and row<3):
            print_P[row][col] = symbol
list2.append(print_P)

#Q
print_Q = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=0 and row<5) or ((row==0 or row==5) and col!=0 and col!=4) or (row-col==2 and row>3):
            print_Q[row][col] = symbol
list2.append(print_Q)

#R
print_R = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or ((row==0 or row==3) and col!=4) or (col==4 and row!=0 and row<3) or (row-col==2):
            print_R[row][col] = symbol
list2.append(print_R)

#S
print_S = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if (row==3 and col!=0 and col!=4) or (row==0 and col!=0) or (row==6 and col!=4) or (col==0 and row!=0 and row<3) or (col==4 and row!=6 and row>3):
            print_S[row][col] = symbol
list2.append(print_S)

#T
print_T = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if row==0 or col==2:
            print_T[row][col] = symbol
list2.append(print_T)

#U
print_U = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row!=6) or (row==6 and col!=0 and col!=4):
            print_U[row][col] = symbol
list2.append(print_U)

#V
print_V = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((col==0 or col==4) and row<5) or (row==5 and col!=0 and col!=4 and col!=2) or (col==2 and row==6):
            print_V[row][col] = symbol
list2.append(print_V)

#W
print_W = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if col==0 or col==4 or (col+row==6 and row>3) or (row-col==2 and row>3):
            print_W[row][col] = symbol
list2.append(print_W)

#X
print_X = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if row==col or col+row==4:
            print_X[row][col] = symbol
list2.append(print_X)

#Y
print_Y = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if ((row==col or col+row==4) and row<3) or (col==2 and row>2):
            print_Y[row][col] = symbol
list2.append(print_Y)

#Z
print_Z = [[" " for i in range(5)] for j in range(7)]
for row in range(7):
    for col in range(5):
        if row==0 or row==6 or (row+col==5):
            print_Z[row][col] = symbol
list2.append(print_Z)

#dipparmar for printing
for i in range(7):
    for j in range(len(list2)):
        for k in range(5):
            print(list2[j][i][k],end=" ")
        print(end=" ")
    print()
