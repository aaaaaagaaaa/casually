#数模第九周  尾坯切割问题

import pulp
import numpy as np

#定义尾坯长度
L_1=62.7
L_2=66

#定义最大最小钢坯运送长度，最大最小合适长度，最优长度
l_min=4.8;l_max=12.6
L_min=9;L_max=10
L_best=9.5
delta_l=0.2#不妨假设切割的精度为0.2米

#定义各个规格的材料可能情形数
short_num=int((L_min-l_min)/delta_l)
middle_num=int((L_max-L_min)/delta_l+1)
long_num=int((l_max-L_max)/delta_l)

def slash_method(L):
    prob=pulp.LpProblem("slash problem",sense=pulp.LpMinimize)
    
    #定义变量 指某种类型工件的数量
    var=[[pulp.LpVariable(f'x{0}_{i}',lowBound=0,cat=pulp.LpInteger) for i in range(0,short_num)],
         [pulp.LpVariable(f'x{1}_{i}',lowBound=0,cat=pulp.LpInteger) for i in range(0,middle_num)],
         [pulp.LpVariable(f'x{2}_{i}',lowBound=0,cat=pulp.LpInteger) for i in range(0,long_num)]]
   
   #定义各个工件的长度 
    short=list(np.arange(l_min,L_min,delta_l))
    middle=list(np.arange(L_min,L_max+delta_l,delta_l))
    long=list(np.arange(L_min+delta_l,l_max,delta_l))
    
    #定义目标函数
    prob+=pulp.lpSum(short[i]*var[0][i] for i in range(0,short_num))
    +pulp.lpSum(+(long[j]-L_max)*var[2][j] for j in range(0,long_num))
    
    #约束条件
    prob+=((sum((short[i]*var[0][i]) for i in range(0,short_num))
    +sum((middle[i]*var[1][i] for i in range(0,middle_num)))
    +sum((long[i]*var[2][i]) for i in range(0,long_num)))==L)
    
    prob.solve()
    
    return {
        'objective':pulp.value(prob.objective),
        'var':[[pulp.value(var[0][i]) for i in range(short_num)],
               [pulp.value(var[1][j]) for j in range(middle_num)],
                [pulp.value(var[2][k]) for k in range(long_num)]]
    }

#输出
print("对于长62.7米的尾坯，方案如下：")
print(slash_method(L_1)['var'])
print('最小剩余值为',slash_method(L_1)['objective'])


print("对于长66米的尾坯,方案如下：")
print(slash_method(L_2)['var'])
print('最小剩余值为',slash_method(L_2)['objective'])
