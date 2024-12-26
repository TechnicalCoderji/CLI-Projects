#dipparmar
def pattern():
    """for alphabet pattern printing

    Returns:
        list: collection of alphabet pattrn od symbol
    """    
    for i in range(len(name)):
        #A
        if name[i] == "A":
            print_A = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and col!=0 and col!=4):
                        print_A[row][col] = symbol
            list2.append(print_A)

        #B
        elif name[i] == "B":
            print_B = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((row==0 or row==3 or row==6) and col!=4) or ((col==0 or col==4) and row!=0 and row!=3 and row!=6):
                        print_B[row][col] = symbol
            list2.append(print_B)

        #C
        elif name[i] == "C":
            print_C = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 and row!=0 and row!=6) or ((row==0 or row==6) and col!=0):
                        print_C[row][col] = symbol
            list2.append(print_C)

        #D
        elif name[i] == "D":
            print_D = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or ((row==0 or row==6) and col<4) or (col==4 and (row>0 and row<6)):
                        print_D[row][col] = symbol
            list2.append(print_D)

        #E
        elif name[i] == "E":
            print_E = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or ((row==0 or row==3 or row==6) and col!=5):
                        print_E[row][col] = symbol
            list2.append(print_E)

        #F
        elif name[i] == "F":
            print_F = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or ((row==0 or row==3) and col!=5):
                        print_F[row][col] = symbol
            list2.append(print_F)

        #G
        elif name[i] == "G":
            print_G = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or row==0 or row==6 or (row==3 and col>1) or (col==4 and row>2):
                        print_G[row][col] = symbol
            list2.append(print_G)

        #H
        elif name[i] == "H":
            print_H = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or row==3:
                        print_H[row][col] = symbol
            list2.append(print_H)

        #I
        elif name[i] == "I":
            print_I = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or row==6 or col==2:
                        print_I[row][col] = symbol
            list2.append(print_I)

        #J
        elif name[i] == "J":
            print_J = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or (row==6 and col<3) or col==2:
                        print_J[row][col] = symbol
            list2.append(print_J)

        #K
        elif name[i] == "K":
            print_K = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or row+col==4 or row-col==2:
                        print_K[row][col] = symbol
            list2.append(print_K)

        #L
        elif name[i] == "L":
            print_L = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==6 or col==0:
                        print_L[row][col] = symbol
            list2.append(print_L)

        #M
        elif name[i] == "M":
            print_M = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (row<3 and (col==row or col+row==4)):
                        print_M[row][col] = symbol
            list2.append(print_M)

        #N
        elif name[i] == "N":
            print_N = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (row<2 and col==1) or (col==2 and row>1 and row<4) or (col==3 and row>3 and row<6):
                        print_N[row][col] = symbol
            list2.append(print_N)

        #O
        elif name[i] == "O":
            print_O = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=0 and row<5) or ((row==0 or row==5) and col!=0 and col!=4):
                        print_O[row][col] = symbol
            list2.append(print_O)

        #P
        elif name[i] == "P":
            print_P = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or ((row==0 or row==3) and col!=4) or (col==4 and row!=0 and row<3):
                        print_P[row][col] = symbol
            list2.append(print_P)

        #Q
        elif name[i] == "Q":
            print_Q = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=0 and row<5) or ((row==0 or row==5) and col!=0 and col!=4) or (row-col==2 and row>3):
                        print_Q[row][col] = symbol
            list2.append(print_Q)

        #R
        elif name[i] == "R":
            print_R = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or ((row==0 or row==3) and col!=4) or (col==4 and row!=0 and row<3) or (row-col==2):
                        print_R[row][col] = symbol
            list2.append(print_R)

        #S
        elif name[i] == "S":
            print_S = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (row==3 and col!=0 and col!=4) or (row==0 and col!=0) or (row==6 and col!=4) or (col==0 and row!=0 and row<3) or (col==4 and row!=6 and row>3):
                        print_S[row][col] = symbol
            list2.append(print_S)

        #T
        elif name[i] == "T":
            print_T = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or col==2:
                        print_T[row][col] = symbol
            list2.append(print_T)

        #U
        elif name[i] == "U":
            print_U = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=6) or (row==6 and col!=0 and col!=4):
                        print_U[row][col] = symbol
            list2.append(print_U)

        #V
        elif name[i] == "V":
            print_V = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row<5) or (row==5 and col!=0 and col!=4 and col!=2) or (col==2 and row==6):
                        print_V[row][col] = symbol
            list2.append(print_V)

        #W
        elif name[i] == "W":
            print_W = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (col+row==6 and row>3) or (row-col==2 and row>3):
                        print_W[row][col] = symbol
            list2.append(print_W)

        #X
        elif name[i] == "X":
            print_X = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==col or col+row==4:
                        print_X[row][col] = symbol
            list2.append(print_X)

        #Y
        elif name[i] == "Y":
            print_Y = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((row==col or col+row==4) and row<3) or (col==2 and row>2):
                        print_Y[row][col] = symbol
            list2.append(print_Y)

        #Z
        elif name[i] == "Z":
            print_Z = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or row==6 or (row+col==5):
                        print_Z[row][col] = symbol
            list2.append(print_Z)

        #0
        elif name[i] == "0":
            print_0 = [[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=0 and row!=6) or ((row==0 or row==6) and col!=0 and col!=4) or row+col==5:
                        print_0[row][col] = symbol
            list2.append(print_0) 
        
        #1
        elif name[i] == "1":
            print_1 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row+col==2 or col==2 or row==6:
                        print_1[row][col] = symbol
            list2.append(print_1)

        #2
        elif name[i] == "2":
            print_2 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==6 or row+col==6 or (row==1 and (col==0 or col==4)) or (row==0 and col!=0 and col!=4):
                        print_2[row][col] = symbol
            list2.append(print_2)

        #3
        elif name[i] == "3":
            print_3 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((row==0 or row==3 or row==6) and col!=0 and col!=4) or (col==4 and row!=0 and row!=3 and row!=6):
                        print_3[row][col] = symbol
            list2.append(print_3)    
        
        #4
        elif name[i] == "4":
            print_4 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==4 or col==3 or col+row==3:
                        print_4[row][col] = symbol
            list2.append(print_4)

        #5
        elif name[i] == "5":
            print_5 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or (col==0 and row<4) or ((row==3 or row==6) and col!=4) or (col==4 and row<6 and row>3):
                        print_5[row][col] = symbol
            list2.append(print_5)
        
        #6
        elif name[i] == "6":
            print_6 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if (col==0 and row!=0 and row!=6) or ((row==3 or row==6) and col!=0 and col!=4) or (row==0 and col!=0) or (col==4 and row<6 and row>3):
                        print_6[row][col] = symbol
            list2.append(print_6)

        #7
        elif name[i] == "7":
            print_7 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if row==0 or row+col==5:
                        print_7[row][col] = symbol
            list2.append(print_7)

        #8
        elif name[i] == "8":
            print_8 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((row==0 or row==3 or row==6) and col!=0 and col!=4) or ((col==0 or col==4) and row!=0 and row!=3 and row!=6):
                        print_8[row][col] = symbol
            list2.append(print_8)
        
        #9
        elif name[i] == "9":
            print_9 =[[" " for i in range(5)] for j in range(7)]
            for row in range(7):
                for col in range(5):
                    if ((row==0 or row==3) and col!=0 and col!=4) or ((col==0 or col==4) and row!=0 and row<3) or (row==6 and col!=4) or (col==4 and row<6 and row>3):
                        print_9[row][col] = symbol
            list2.append(print_9)

        #for space
        elif name[i] == " ":
            print_space = [[" " for i in range(5)] for j in range(7)]
            list2.append(print_space)
            
        else:
            print("invalid input.")

    return list2


symbol = input("enter your symbol for print:") # for input symbol from user
name = input("enter you want to print:") # for input string to print from user
name = name.upper() # convert string to upper case
list2 = [] # make empty list 
list3 = pattern() # call pattern function

# neted loops to print name in horizontal line
for i in range(7):
    for j in range(len(list3)):
        for k in range(5):
            print(list3[j][i][k],end=" ")
        print(end=" ")
    print()