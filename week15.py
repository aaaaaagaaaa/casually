#第十五周  图论模型  矩阵摹乘

import numpy as np

def find_min(a,b):
    #矩阵摹乘的每个元的计算
    A=[]
    for i in range(0,7):
        A.append(a[i]+b[i])
    return min(A)  

def prod(A):
    #矩阵摹乘
    B=np.empty((7,7))
    for i in range(0,7):
        for j in range(0,7):
            B[i][j]=find_min(A[i],A[j])#由于无向图 权矩阵具有对称性 第j列同于第j行
    return B

D_1=np.array([[0,3,4,7,100,100,100],[3,0,3,2,4,100,100],[4,3,0,100,5,7,100],[7,2,100,0,2,100,6],
[100,4,5,2,0,1,4],[100,100,7,100,1,0,2],[100,100,100,6,4,2,0]])

#获取D1-D10
D=[]
D.append(D_1)
for i in range(0,10):
    D.append(prod(D[i]))#D中第i个元素为D_i+1
#print(D[3])

h=np.array([40,25,45,30,20,35,50])#各村的小学生数量 权重
H=[]#用于储存每个村庄为学校时的小学生路程总和
for i in range(0,7):
    H.append(np.dot(h,D[3][i]))
print(H)

