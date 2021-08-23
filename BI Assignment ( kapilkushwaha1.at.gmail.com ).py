# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:39:02 2021

@author: KapilK
"""

import pandas as pd
import pandas.plotting 
import numpy as np
import matplotlib.pyplot as plt

import plotly.express as px
import plotly.graph_objects as go
from matplotlib.colors import LogNorm 


file = "C:/Users/KapilK/Downloads/Job Assignment/Convosight/BI Assignment - Data.xlsx"
cmaps = ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu','RdYlBu', 'RdYlGn', 'Spectral']

d = pd.read_excel(file,sheet_name='text')
d_txt = pd.DataFrame(d,index=None)
#print("Excel text : ", d_txt.info())

d2 = pd.read_excel(file,sheet_name='numbers')
d_num = pd.DataFrame(d2,index=None)
#print("Excel numbers : ", d_num.info())

months = d2.drop(['Keywords','category','super category'],axis=1)
d_months= list(months.columns)
keywd = d_num['Keywords']
cat = d_num['category']
scat = d_num['super category']
total = np.zeros(months.shape[0])
for index, row in months.iteritems():
    total = total + row
d_num['Totals'] = total

group_dnum = d_num.groupby(['category','Keywords','super category','Totals']).size().reset_index().rename(columns={0:'sum'})
group_dnum = pd.DataFrame(group_dnum, index = None)
group_dnum.drop(['sum'],axis=1,inplace = True)
print(group_dnum)

print("color : ",len(cmaps))
i=0
p = []

for x in months:
    i = ( (i+1) if i < (len(cmaps)-1) else 0 )
    #print(i,cmaps[i])
    plt.bar(  d_num['category'],d_num[x]) #cmap=cmaps[i]
    plt.xlabel('category')
    plt.ylabel('Totals' +" "+ x)
    plt.show()

group_by_category = d_num.groupby(['category']).size().reset_index().rename(columns={0:'sum'})
gc = np.array(group_by_category)
gc = np.transpose(gc)
print(gc[0])
plt.bar( gc[0],height=gc[1],width=0.5,data = gc,color='cyan')
plt.xlabel('Category')
plt.ylabel('count of Keywords')
plt.show()










