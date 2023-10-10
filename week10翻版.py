import numpy as np
import openpyxl
from pulp import*
import statsmodels.api as sm

file='/Users/lvangge/Desktop/副本古塔变形分析data.xlsx'
workbook=openpyxl.load_workbook(file)
sheet=workbook.active

def get_floor13(char):#获取13层的已知数据
    x=[]
    for i in range(99,107):
        x.append(sheet[char][i].value)
    for i in x:
        if i==None:
            x.remove(i)
    return x

def get_coordinate(char):#获取前面12层的坐标函数
    coordinate=[]
    for i in range(0,12):
        coordinate.append(sheet[char][8*(i+1)-1].value)
    return coordinate    

def linear_func(x_floor13,y_floor13,z_floor13):#获取13层的平面方程函数
    date=[[x_floor13[i],y_floor13[i] ]for i in range(0,7)]
    x=sm.add_constant(date)
    model=sm.OLS(z_floor13,x)
    result=model.fit()
    print("打印拟合平面信息：")
    print(result.summary())

#获取13层的已知点坐标
x1_13_coordinate=get_floor13('C')
y1_13_coordinate=get_floor13('D')
z1_13_coordinate=get_floor13('E')

x2_13_coordinate=get_floor13('I')
y2_13_coordinate=get_floor13('J')
z2_13_coordinate=get_floor13('K')

#获取13层的平面方程
linear_func(x1_13_coordinate,y1_13_coordinate,z1_13_coordinate)
linear_func(x2_13_coordinate,y2_13_coordinate,z2_13_coordinate)

#测量1输出结果：-0.0267x-0.006y+64.5308=z
def func1_of_z(x,y):
    return -0.0267*x+0.0066*y+64.5308

#测量2输出结果：-0.0271*x+0.070*y+64.5489=z
def func2_of_z(x,y):
    return -0.0271*x+0.0070*y+64.5489

def linear_regression(x,y):#拟合每层某位置的函数
    N=len(x)
    sumx=sum(x)
    sumy=sum(y)
    sumx2=np.dot(x,x)
    sumxy=np.dot(x,y)
    
    A=np.mat([[N,sumx],[sumx,sumx2]])
    b=np.array([sumy,sumxy])
    
    return np.linalg.solve(A,b)

def xy_of_floor13(coordinate):
    a_0,a_1=linear_regression(range(1,13),coordinate)
    return a_0+13*a_1

#获取前12层的第5位置的坐标
x1_coordinate=get_coordinate('C')
y1_coordinate=get_coordinate('D')
z1_coordinate=get_coordinate('E')

x2_coordinate=get_coordinate('I')
y2_coordinate=get_coordinate('J')
z2_coordinate=get_coordinate('K')

#获取缺失数据的xy坐标
x1_13=xy_of_floor13(x1_coordinate)
y1_13=xy_of_floor13(y1_coordinate)
x2_13=xy_of_floor13(x2_coordinate)
y2_13=xy_of_floor13(y2_coordinate)

#获取缺失数据的z坐标
z1_13=func1_of_z(x1_13,y1_13)
z2_13=func2_of_z(x2_13,y2_13)

#打印
print("第一次测量的缺失数据为：x=",x1_13,"y=",y1_13,"z=",z1_13)
print("第二次测量的缺失数据为：x=",x2_13,"y=",y2_13,"z=",z2_13)

