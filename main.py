import math

#Zad. 1 lab1
'''
float = 250.43
float1 = 120.65
int = 5
int1 = 6
string = 'łańcuch znaków'
string1 = 'łańcuch znaków1'
complex = 5+6j
complex1 = 3+2j
print(float)
print(float1)
print(int)
print(int1)
print (string)
print(string1)
print (complex)
print(complex1)
'''

#zad. 2 lab1
'''
dodawanie = 2 + 2
odejmowanie = 5 - 2
mnozenie = 3 * 3
dzielenie = 6 / 3
dzieleniecal = 9 // 2
reszta = 9 % 2
potega = 2 ** 4
print(dodawanie)
print(odejmowanie)
print(mnozenie)
print(dzielenie)
print(dzieleniecal)
print(reszta)
print(potega)
'''

#zad. 3 lab1
'''
op_przyr = 6
op_przyr += 1
op_przyr -= 1
op_przyr *= 2
op_przyr /= 3
op_przyr %= 4
op_przyr **= 2
'''

#zad. 4 lab1
'''
e = 2
potega = e ** 10
pierwiastek = pow(math.log(5+pow(math.sin(8),2)),1/6)
wartosc_bezwzgledna = math.fabs(-3.55)
wartosc_bezwzgledna1 = math.fabs(-4.80)
print(potega)
print(pierwiastek)
print(wartosc_bezwzgledna)
print(wartosc_bezwzgledna1)
'''

#zad. 5 lab1
'''
imie = "WIKTOR"
nazwisko =  "KOWALCZYK"
imie = imie.capitalize()
nazwisko = nazwisko.capitalize()
print(imie + " " + nazwisko)
'''

#zad. 6 lab1
'''
tekst = "la la la la la la la la"
liczba_slow_la = tekst.count("la")
print(liczba_slow_la)
'''


#zad. 7 lab1
'''
zmienna_lancuchowa = "lubie muzyke z gatunku rap"
print(zmienna_lancuchowa[1])
print(zmienna_lancuchowa[len(zmienna_lancuchowa) - 1])
'''

#zad. 8 lab1
'''
print(tekst.split(" "))
'''

#zad. 9 lab1
'''
string = "łańcuch znakowy"
liczba_float = 5
hexadecymalny = 0x95
print(str(string))
print(float(liczba_float))
print(hex(hexadecymalny))
'''

#zad. 1 lab2
'''
lista_ulubionych_sportow = ["piłka nożna", "siatkówka", "koszykówka"]
lista_ulubionych_sportow.reverse()
lista_ulubionych_sportow.append("tenis stołowy")
lista_ulubionych_sportow.append("tenis ziemny")
print(lista_ulubionych_sportow)
'''

#zad. 2 lab2
'''
slownik_gazeta = {'cdn.' : 'Ciąg dalszy nastąpi', 'itd.' : 'i tak dalej', 'np.' : 'na przykład'}
'''

#zad. 3 lab2
'''
lista_gier = {'cs go' : 'Counter Strike: Global Offensive', 'cs 1.6' : 'Counter Strike 1.6', 'lol' : 'League of Legends', 'mohaa' : 'Medal of Honor Allied Asault'}
liczba_gier = str(len(lista_gier.keys()))
'''

#zad. 4 lab2
'''
licznik_a = 0
print("Napisz jakieś zdanie: ")
zdanie_a = input()
for a in range(len(zdanie_a)):
    if zdanie_a[a] == 'a':
        licznik_a+=1

print("Liczba liter a w zdaniu to: " + str(licznik_a))
'''

#zad. 5 lab2
'''
liczby = open('liczby.txt', 'r')
liczba1 = int(liczby.readline())
liczba2 = int(liczby.readline())
liczba3 = int(liczby.readline())
dzialanie = pow(liczba1, liczba2) + liczba3
liczby.close()
liczby = open('liczby.txt', 'a')
liczby.write("\n" + str(dzialanie))
liczby.close()
'''

#zad. 6 lab2
'''
a = 687
b = 223
c = 116
if a>b:
    if a>c:
        najwieksza_liczba = a
    else:
        najwieksza_liczba = c
else:
    if b>c:
        najwieksza_liczba = b
    else:
        najwieksza_liczba = c

print("Największa liczba to: " + str(najwieksza_liczba))
'''
#zad. 7  lab2
'''
liczby_int_for = [15, 38.67, 29, 40.32, 45, 60.87]
for a in range(len(liczby_int_for)):
    liczby_int_for[a] **= 2
'''

#zad. 8 lab2
'''
liczby_parzyste = []
x = 0
while x <= 9:
    a = input()
    a = int(a)
    x += 1
    if a % 2 == 0:
        liczby_parzyste.append(a)

print(liczby_parzyste)
'''

#zad. 9 lab2
'''
liczba = input()
liczba = int(liczba)
if liczba<0:
    print("Liczba musi być dodatnia")

else:
    wynik = math.sqrt(liczba)
    print(wynik)
'''



