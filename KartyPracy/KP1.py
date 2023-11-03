# Karta pracy nr 3b
import calendar
from math import sqrt as pierwiastek

# Zadanie 1
def zadanie1():
    rok = 2022
    miesiac = 11
    kalendarz = calendar.month(rok, miesiac)
    print(kalendarz)

# Zadanie 2
def zadanie2():
    for i in range(1, 10, 2):
        print(i ** 2)

# Zadanie 3
def zadanie3():
    for i in range(1000, 10000):
        if i % 379 == 0:
            print(i)

# Zadanie 4
def zadanie4():
    for i in range(100, 1000):
        if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
            print(i)

# Zadanie 5
def zadanie5():
    n = int(input("Podaj liczbę n: "))
    suma = 0
    for i in range(n):
        num = int(input(f"Podaj liczbę: "))
        suma += num
    print(f"Suma: {suma}")

# Zadanie 6
def zadanie6():
    k = int(input("Podaj liczbę k: "))
    suma = 0
    for i in range(2, 2 * k + 1, 2):
        suma += i
    print(f"Suma: {suma}")

# Zadanie 7
def zadanie7():
    m = int(input("Podaj liczbę m: "))
    suma = 0
    for i in range(11, 2 * m + 11, 2):
        suma += i
    print(f"Suma: {suma}")

# Zadanie 8
def zadanie8():
    W0 = float(input("Podaj kwotę wejściową W0: "))
    L = float(input("Podaj okres inwestycji w latach L: "))
    n = int(2 * L)  # Zakładamy kapitalizację co pół roku
    roczna_stopa_procentowa = 6.0
    miesieczna_stopa_procentowa = roczna_stopa_procentowa / 12 / 100

    for _ in range(n):
        W0 += W0 * miesieczna_stopa_procentowa

    print(f"Wartość inwestycji po {L} latach wynosi: {W0:.2f}")

# Zadanie 9
def zadanie9():
    n = int(input("Podaj liczbę n: "))
    suma = 0
    for i in range(1, n + 1):
        suma += 21 * i
    print(f"Suma: {suma}")

# Zadanie 10
def zadanie10():
    for i in range(1, 1001):
        if i % 10 == pierwiastek(i) or i % 100 == pierwiastek(i):
            print(i)

# Wybór zadania
try:
    numer_zadania = int(input("Wybierz numer zadania (od 1 do 10): "))
    if numer_zadania == 1:
        zadanie1()
    elif numer_zadania == 2:
        zadanie2()
    elif numer_zadania == 3:
        zadanie3()
    elif numer_zadania == 4:
        zadanie4()
    elif numer_zadania == 5:
        zadanie5()
    elif numer_zadania == 6:
        zadanie6()
    elif numer_zadania == 7:
        zadanie7()
    elif numer_zadania == 8:
        zadanie8()
    elif numer_zadania == 9:
        zadanie9()
    elif numer_zadania == 10:
        zadanie10()
    else:
        print("Nieprawidłowy numer zadania. Wybierz liczbę od 1 do 10.")
except ValueError:
    print("Podana wartość nie jest liczbą.")
