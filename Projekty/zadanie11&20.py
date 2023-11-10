# zadanie 11
from math import sqrt
a, b, c = int(input()), int(input()), int(input())

delta = b ** 2 - 4 * a * c
if delta < 0:
    x1 = -b + sqrt(-delta) / (2 * a)
    x2 = -b - sqrt(-delta) / (2 * a)
    print(x1, x2)
elif delta == 0:
    x1 = (-b / (2 * a))
    print(x1)
else:
    print("Brak pierwistków")

# zadanie 20
# Program losuje liczbę z zakresu od 1 do 100. Zadaniem gracza jest odgadnięcie tej liczby. Jeżeli użytkownik poda za dużą liczbę program wyświetli komunikat „Szukana wartość jest mniejsza”. Jeżeli wprowadzi za małą liczbę program wyświetli „Szukana wartość jest większa”. Po odgadnięciu liczby gracz dowiaduje się po ilu próbach udało mu się zakończyć grę.
import random
liczba = random.randint(1, 100)
print(liczba)
proba = 1
zgadnieta = int(input("Podaj liczbę: "))
while liczba != zgadnieta:
    if zgadnieta > liczba:
        print("Szukana wartość jest mniejsza")
    else:
        print("Szukana wartość jest większa")
    zgadnieta = int(input("Podaj liczbę: "))
    proba += 1
print(proba)
