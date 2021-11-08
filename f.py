import numpy as np
import copy
from collections import Counter
T=[[0.1,0,0.2,0.8,0.3,0.0,0.5,0.6,0,0.1,0.3,0.1,0.2,0.2,0.1,0.2],[0.7,0.5,0.2,0.1,0.0,0.4,0.0,0.3,0.5,0.6,0.2,0.5,0,0.6,0.7,0.4]
    ,[0.2,0.5,0.2,0.0,0.4,0,0.4,0,0.1,0,0.1,0.4,0.2,0.1,0.1,0.2],[0,0,0.4,0.1,0.3,0.6,0.1,0.1,0.4,0.3,0.4,0,0.6,0.1,0.1,0.2]]
print(len(T[0]))
print(len(T[1]))
print(len(T[2]))
print(len(T[3]))

R=[]
for i in range(0,16):
    R.append([])
    for j in range(0,16):
        R[i].append(999)


m=4
for i in range(0,16):
    for j in range(0,16):
        U=0
        LL=0
        LR=0
        for k in range(0,m):
            U=U+T[k][i]*T[k][j]
        for k in range(0,m):
            LL= LL+(T[k][i]**2)
        for k in range(0,m):
            LR = LR + (T[k][j] ** 2)
        R[i][j]=U/((LL*LR)**0.5)

for i in range(0,16):
    print(R[i])


c=[[1,0.8,0.4,0.5,0.2],[0.8,1,0.4,0.5,0.9],[0.4,0.4,1,0.4,0.4],[0.5,0.5,0.4,1,0.5],[0.2,0.9,0.4,0.5,1]]
def Get_O(Matrix):
    rowlen=len(Matrix)
    columnlen=len(Matrix)
    result=[]
    for i in range(0,rowlen):
        result.append([])
        for j in range(0,columnlen):
            result[i].append(0)
    for i in range(0,rowlen):
        for j in range(0,columnlen):
            if i!=j:
                midlist=[]
                for k in range(0,rowlen):
                    midlist.append(min(Matrix[i][k],Matrix[k][j]))
                result[i][j]=max(midlist)
            else:
                result[i][j]=Matrix[i][j]
    return result
# R1=Get_O(R)
# for i in range(0,16):
#     print(R1[i])

flag=0
R1=R
h=1
while flag!=1:
    R2=Get_O(R1)
    if R2==R1:
        flag=1
    else:
        R1=R2
        h=h+1
for i in range(0,16):
    print(R2[i])
print(h)
print('question 3')
R_04=copy.deepcopy(R2)
R_08=copy.deepcopy(R2)
print('r_08')
for i in range(0,16):
    for j in range(0,16):
        if R_08[i][j]>=0.8:
            R_08[i][j]=1
        else:
            R_08[i][j] = 0
for i in range(0,16):
    print(R_08[i])
print('r_04')
for i in range(0,16):
    for j in range(0,16):
        if R_04[i][j]>=0.4:
            R_04[i][j]=1
        else:
            R_04[i][j] = 0
for i in range(0,16):
    print(R_04[i])

print('question 4')

def Find_Num(R):
    number=[]
    for i in range(0, 16):
        if number.count(R[i]) == 0:
            number.append(R[i])
    a=len(number)
    return a

good_threshold=[]
for i in range(800000,1000000):

    threshold=i/1000000
    print(threshold)
    R3=copy.deepcopy(R2)
    for j in range(0,16):
        for k in range(0,16):
            if R2[j][k]>=threshold:
                R3[j][k]=1
            else:
                R3[j][k]=0
    num=Find_Num(R3)
    if num==3:
        good_threshold.append(threshold)
print('the suitable cut number is:')
print(good_threshold)
