import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


values = [21, 27, 33, 15, 35]
indexes = ['A', 'B', 'C', 'D', 'E']

s = pd.Series(values, index=indexes) #ustala typ danych w zmiennej
                                     # (index - wybór zmiennej dla której ma być pokazany typ zmiennej)

s.plot( kind='pie', #styl wykresu(kolowy, slupkowy)
        fontsize=12, #rozmiar czcionki
        figsize=(6, 6), #rozmiar okna
        colors=['#d82647', '#2af6ea', '#af768a', '#a2d1ef', '#7c1b53'], #kolory
        title='Tytuł',
        ylabel='',
        labels=values, #napis przy wykresie(zmienna - values)
        counterclock=True,
        startangle=90)

plt.legend(loc='upper left', labels=indexes) #loc - miejsce gdzie ma sie znalezc legenda
                                             #labesl - jakie dane ma wyswietlac

plt.show()
#plt.savefig('./zadanie1.pdf')


'''
xlsx = pd.ExcelFile('2020e01/ceny.xlsx')
df = pd.read_excel(xlsx, header=0)

print(df.where(df['Rok'] == 2017).groupby('Rodzaje towarów i usług').mean())

df.set_index('Miesiące', inplace=True)

df.groupby('Rodzaje towarów i usług')['Wartosc'].plot(
    xlabel='Miesiąc',
    ylabel='Wartość',
    title='Wartość produktów w miesiącach'
)

plt.legend(loc='upper left')
plt.show()
#plt.savefig('2020-e01/zadanie2.jpg')
'''

'''
df = pd.read_csv('2020e01/gastro.csv', header=0, sep=';', decimal='.')
df.set_index('Typy placówek', inplace=True)
df = df.transpose()

df = df.reset_index()
df = df.rename_axis(None, axis=1)
df = df.rename(columns={'index': 'Typy placówek'})

df.pivot('Rok', 'Typy placówek', 'Wartosc').plot(
    kind='bar',
    xlabel='Lata',
    ylabel='Wartosc',
    rot=0,
    title='Wartość placówek',
    figsize=(10,10))
plt.legend(loc='upper left', labels=('Bary 2015', 'Bary 2016', 'Bary 2017',
           'Punkty gastronomiczne 2015', 'Punkty gastronomiczne 2016', 'Punkty gastronomiczne 2017',
           'Restauracje 2015', 'Restauracje 2016', 'Restauracje 2017',
           'Stołówki 2015', 'Stołówki 2016', 'Stołówki 2017'))

plt.show()
#plt.savefig('wykres2020e01.png')
'''