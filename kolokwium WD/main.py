import numpy as np
import pandas as pd

'''
a = np.arange(2)

print(a)
'''

'''
a = np.array([0, 1]) # == a = np.arange(2)

print(type(a))
print(a.dtype)
'''

'''
a = np.arange(2, dtype = 'int64')
print(a.dtype)

b = a.astype('float')

print(b)
print(b.dtype)
print(b.shape)#rozmiar tablicy
print(a.ndim) #ilość wymiarów tablicy
'''

'''
m = np.array([np.arange(2), np.arange(2)]) #talica wielowymiarowa
print(m.shape)
print(type(m))
'''
'''
zera = np.zeros((5,5))
jedynki = np.ones((4,4))
print(zera)
print(jedynki)
print(zera.dtype)
print(jedynki.dtype)

pusta = np.empty((2,2)) #pusta macierz (wiersze, kolumny)
print(pusta)

poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)
'''

'''
macierz = np.array([[1,2], [3,4]])
print(macierz)
'''

'''
liczby = np.arange(1,2,0.1)
print(liczby)
'''

'''
liczby_lin = np.linspace(1,2,5)
print(liczby_lin)
'''

'''
mat_diag = np.diag([a for a in range(5)])
print(mat_diag)

mat_diag_k = np.diag([a for a in range(5)], -1)
print(mat_diag_k)
'''

#zad1
'''
a = np.arange(3,46,3)
print(a)

'''

#zad2
'''
a = np.arange(1.1, 5.2, 0.2, dtype='float')
b = a.astype('int64')

print(a)
print(b)
'''

#zad3

'''
n = 5
def funkcja(n):
    a = np.arange(n * n)
    b = a.reshape((n, n))
    return b

x = funkcja(n)
print(x)
'''

#zad4

'''
podstawa = 2
ilosc = 4

def zadanie(podstawa, ilosc):

    wynik = np.logspace(1, ilosc, num=ilosc, base=podstawa, dtype=int)
    
    return wynik

print(zadanie(podstawa, ilosc))
'''

#zad5

'''
def zadanie2(n):
    lista = [*range(1, n, 1)]
    lista.reverse()
    mat_diag = np.diag(lista)
    print(mat_diag)

print(zadanie2(8))
'''

# ------------------------------------------PANDAS-----------------------------------------------------------------------

'''
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)
s1 = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Elonora'])
print(s1)
'''

'''
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)
print(df.dtypes)
'''

'''
daty = pd.date_range('20210324', periods = 5) #periods-ilosc kolejnych dat
print(daty)
df = pd.DataFrame(np.random.randn(5,4), index=daty, columns=list('ABCD'))
print(df)
'''

'''
df = pd.read_csv('dane.csv', header=0, sep=";", decimal=',')
print(df)
df.to_csv('plik.csv', index=False)
'''

'''
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
df.to_excel('wyniki.xlsx', sheet_name='arkusz pierwszy')
'''

'''
s = pd.Series([10, 12, 8, 14], index=['Ala', 'Marek', 'Wiesiek', 'Elonora'])

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
'''

#print(s['Wiesiek'])
#print(s.Wiesiek)

#print(df[0:4])
#print("")

#print(df['Populacja'])
#print(df.iloc[[0],[0]])
#print(df.loc[[1], ["Kraj"]])
#print(df.at[2, "Kraj"])

#print('kraj: ' + df.Kraj)

#print(df.sample()) #losowy element
#print(df.sample(2)) #losowe n elementow
#print(df.sample(frac=0.5)) #losowe % elementow
#print(df.sample(n=10, replace=True)) #losowanie z powtorzeniami

#print(df.head())
#print(df.head(2))
#print(df.tail(1))

#print(df.describe())
#print(df.T)

#print(s[(s>9)])
#print(s.where(s > 10))
#print(s.where (s>10, 'za małe'))

'''
seria = s.copy()
seria.where(seria > 10, 'za małe', inplace=True)
print('########')
print(seria)
'''

#print(s[~(s > 10)])
#print(s[(s < 13) & (s > 8)])

#print(df[df['Populacja']>1200000000])
#print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])

'''
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))
'''

'''
s['Wiesiek'] = 15
print(s.Wiesiek)
s['Alan'] = 16
print(s)
'''

'''
df.loc[3] = 'dodane'
print(df)
'''

'''
df.loc[3] = ['Polska', 'Warszawa', 38675467]
#print(df)
'''

'''
new_df = df.drop([3])
print(new_df)
'''

'''
df.drop([3], inplace=True)
print(df)
'''

'''
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
#print(df)
'''

#print(df.sort_values(by='Kraj'))

'''
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
'''

#print(df.groupby(['Kontynent']).agg({'Populacja': ['sum']}))

#zad1

'''
xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
#print(df)
'''

#zad2

#print(df[df['Liczba']>1000])
#print(df[df.Imie == 'WIKTOR'])
#print(df.agg({'Liczba':['sum']}))
#print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)])
#print(df.groupby(['Plec']).agg({'Liczba' : ['sum']}))
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
#print(df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).first())
#new_df = df.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec'])
#for index, group in enumerate(new_df, start=1):
#print(f"{index} {group[0]}")
#print(f" {group[1].iloc[0]['Imie']}", end='')
#print(f" {group[1].iloc[0]['Liczba']}")
#print('')
#print("Chłopiec")
#print(df[df['Plec'] == 'M'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),                                                                                  ascending=False).iloc[0])
#print("Dziewczynka")
#print(df[df['Plec'] == 'K'].groupby(['Imie']).agg({'Liczba': ['sum']}).sort_values(('Liczba', 'sum'),                                                                                  ascending=False).iloc[0])

#zad3

#df = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')

#print(df['Sprzedawca'].unique())
#print('')
#print(df.sort_values('Utarg', ascending=False).head(5))
#print('')
#print(df.groupby('Sprzedawca').size())
#print('')
#print(df.groupby('Kraj').agg({'Utarg': ['sum']}))
#print(df.groupby('Kraj').size())
#print('')
#print(df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')].
#      agg({'Utarg': ['sum']}))
#print('')
#print(df[df['Data zamowienia'].str[:4] == '2004'].agg({'Utarg': ['mean']}))
#rok_2004 = df[((df[ 'Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31'))]
#rok_2004.to_csv("zamowienia_2004.csv", index=False)








#zad3

df = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal='.')
#print(df)

#print(df['Sprzedawca'].unique())
#print(df.sort_values(['Utarg']).head(5))

#print(df.groupby(['Sprzedawca']).size())
#lub
#print(df.groupby(['Sprzedawca']).agg({'idZamowienia' : ['count']}).sort_values(('idZamowienia', 'count'), ascending=False))

#print(df.groupby(['Kraj']).size())
#print(df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31') & (df['Kraj'] == 'Polska')])
#print(df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')].agg({'Utarg': ['mean']}))

'''
zamowienia_2004 = df[(df['Data zamowienia'] >= '2004-01-01') & (df['Data zamowienia'] <= '2004-12-31')]
zamowienia_2004.to_csv('zamowienia_2004.csv', index=False)
zamowienia_2005 = df[(df['Data zamowienia'] >= '2005-01-01') & (df['Data zamowienia'] <= '2005-12-31')]
zamowienia_2005.to_csv('zamowienia_2005.csv', index=False)
'''