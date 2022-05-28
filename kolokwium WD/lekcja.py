import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

'''
plt.plot([1,2,3,4])
plt.ylabel('jakieś liczby')
plt.show()
'''

''''
plt.plot([1,2,3,4], [1,4,9,16], 'gs-')
plt.axis([0, 6, 0, 20]) #xmin, xmax, ymin, ymax
plt.show()
'''

'''
plt.plot([1,2,3,4,], [1,4,9,16], 'r')
plt.plot([1,2,3,4,], [1,4,9,16], 'o')
plt.axis([0, 6, 0, 20])
plt.show()
'''

'''
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.legend(labels=['liniowa', 'kwadratowa', 'szescienna'])
plt.show()
'''

'''
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='liniowa')
plt.plot(x, x**2, label="kwadratowa")
plt.plot(x, x**3, label='szceścienna')
plt.xlabel('etykieta x')
plt.ylabel('etykieta y')
plt.title("Prosty wykres")
plt.legend()
plt.show()
'''

'''
x = np.arange(0, 10,0.1)
s = np.sin(x)
plt.plot(x, s, 'r--', label="sin(x)")
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x)')

plt.legend()
plt.show()
'''

'''
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100
print(f"a={data['a'][0]}, b={data['b'][0]}, c={data['c'][0]}, d={data['d'][0]}")
plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.show()
'''

'''
x1 = np.arange(0, 2, 0.02)
x2 = np.arange(0, 2, 0.02)

y1 = np.sin(2* np.pi * x1)
y2 = np.cos(2* np.pi * x2)

plt.subplot(2, 1, 1,)
plt.plot(x1, y1, '-')
plt.title('wykres sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.subplot(2, 1, 2)
plt.plot(x2, y2, 'r-')

plt.xlabel('x')
plt.ylabel('cos(x)')
plt.title('wykres cos(x)')
plt.subplots_adjust(hspace=0.5)
plt.show()
'''

'''
x1 = np.arange(0.0, 2.0, 0.02)
x2 = np.arange(0.0, 2.0, 0.02)
x = np.linspace(1, 100, 100)

y1 = np.sin(2 * np.pi * x1)
y2 = np.cos(2 * np.pi * x2)

fig, axs = plt.subplots(3, 2)
axs[0,0].plot(x1, y1, '-')
axs[0,0].set_title('wykres sin(x)')
axs[0,0].set_xlabel('x')
axs[0,0].set_ylabel('sin(x)')

axs[1,1].plot(x2, y2, 'r--')
axs[1,1].set_title('wykres cos(x)')
axs[1,1].set_xlabel('x')
axs[1,1].set_ylabel('cos(x)')

axs[2,0].plot(x, x**2, 'g:')
axs[2,0].set_title('Funkcja kwadratowa')
axs[2,0].set_xlabel('x')
axs[2,0].set_ylabel('y')

fig.delaxes(axs[0,1])
fig.delaxes(axs[1,0])
fig.delaxes(axs[2,1])

plt.show()
'''

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska', ],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Populacja': [11190846, 1303171035, 207847528, 38645467],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']}

df=pd.DataFrame(data)
print(df)
