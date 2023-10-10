#数模第四周-投入产出模型：计算一个矩阵的逆阵
import numpy as np 

T=np.array([[0.2,0.3,0.2],[0.4,0.1,0.2],[0.1,0.3,0.2]])#投入系数阵
I=np.array([[1,0,0],[0,1,0],[0,0,1]])#单位阵

C=np.linalg.inv(I-T)
print("Here is the inverse:\n",C)
