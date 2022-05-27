import pandas as pd
import matplotlib.pyplot as plt

'''
indexes = ['A', 'B', 'C', 'D', 'E']
values = [21, 27, 33, 15, 35]

s = pd.Series(values, index=indexes)

s.plot(kind='pie',
       title='Tytuł',
       figsize=(6, 6),
       labels=values,
       colors=['#d82647', '#2af6ea', '#af768a', '#a2d1ef', '#7c1b53'],
       startangle=90,
       ylabel='',

       )

plt.legend(loc='upper left', labels=indexes)
plt.savefig('2020e01zad1.png')
'''

df = pd.read_csv('2020e02/gastro.csv', header=0, sep='@', decimal='.')
df.set_index('Typy placówek', inplace=True)
df = df.transpose()
