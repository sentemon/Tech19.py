# Karta Pracy nr 3

# Zadanie 1
def zadanie1(n):
    wynik = []
    for i in range(1, n + 1):
        wynik.append(str(i ** 3 + 3))
    return ", ".join(wynik)

# Zadanie 2
def zadanie2():
    wynik = []
    for i in range(105, 1000, 15):
        wynik.append(str(i))
    return ", ".join(wynik)

# Zadanie 3
def zadanie3(n):
    wynik = []
    for i in range(1, n + 1):
        if n % i == 0:
            wynik.append(str(i))
    return ", ".join(wynik)

# Zadanie 4
def zadanie4():
    suma = 0
    for i in range(10, 100):
        suma += i
    return str(suma)

# Zadanie 5
def zadanie5(n, tajemnicza_liczba):
    for x in range(1, n):
        if x != tajemnicza_liczba:
            return str(x)

# Zadanie 6
def zadanie6(n):
    fib = [1, 2]
    for i in range(2, n):
        next_term = fib[i - 1] + fib[i - 2]
        fib.append(next_term)
    return ", ".join(map(str, fib))

try:
    numer_zadania = int(input("Podaj numer zadania od 1 do 6: "))
    
    if numer_zadania == 1:
        n = int(input("Podaj n: "))
        wynik = zadanie1(n)
    elif numer_zadania == 2:
        wynik = zadanie2()
    elif numer_zadania == 3:
        n = int(input("Podaj liczbę n: "))
        wynik = zadanie3(n)
    elif numer_zadania == 4:
        wynik = zadanie4()
    elif numer_zadania == 5:
        n = int(input("Podaj n: "))
        tajemnicza_liczba = int(input("Podaj tajemniczą liczbę x: "))
        wynik = zadanie5(n, tajemnicza_liczba)
    elif numer_zadania == 6:
        n = int(input("Podaj n: "))
        wynik = zadanie6(n)
    else:
        wynik = "Podano nieprawidłowy numer zadania."

    print("Wyjście:", wynik)

except ValueError:
    print("Podano nieprawidłowe dane.")
