# Karta Pracy nr 2

# Zadanie 1
def zadanie1(a):
    if a % 3 == 0:
        return "TAK"
    else:
        return "NIE"

# Zadanie 2
def zadanie2(a):
    if len(len(str(a))) == 3 and a % 17 == 0:
        return "TAK"
    else:
        return "NIE"

# zadanie 3
def zadanie3(yo):
    if yo >= 18:
        return "TAK"
    else:
        return "NIE"

# Zadanie 4
def zadanie4(waga):
    limit = 20
    if waga <= limit:
        return "TAK"
    else:
        return "NIE"

# Zadanie 5
def zadanie5(a, b, c):
    if (a < c and b > c) or (b < c and a > c):
        return "TAK"
    else:
        return "NIE"

# Zadanie 6
def zadanie6(a, p):
    if ((a**p - a) % p == 0):
        return "TAK"
    else:
        return "NIE"

# Zadanie 7
def zadanie7(p, k, s):
    if p + 3 * s >= k:
        return "TAK"
    else:
        return "NIE"

try:
    numer = int(input("Podaj nr zadania od 1 do 7: "))
    if 1 <= numer <= 7:
        if numer == 1:
            a = int(input("Podaj liczbę dla zadania 1: "))
            print(zadanie1(a))
        elif numer == 2:
            a = int(input("Podaj liczbę dla zadania 2: "))
            print(zadanie2(a))
        elif numer == 3:
            yo = int(input("Podaj wiek dla zadania 3: "))
            print(zadanie3(yo))
        elif numer == 4:
            waga = int(input("Podaj wagę dla zadania 4: "))
            print(zadanie4(waga))
        elif numer == 5:
            a = int(input("Podaj pierwszą liczbę dla zadania 5: "))
            b = int(input("Podaj drugą liczbę dla zadania 5: "))
            c = int(input("Podaj trzecią liczbę dla zadania 5: "))
            print(zadanie5(a, b, c))
        elif numer == 6:
            a = int(input("Podaj liczbę a dla zadania 6: "))
            p = int(input("Podaj liczbę p dla zadania 6: "))
            print(zadanie6(a, p))
        elif numer == 7:
            p = int(input("Podaj pierwszą liczbę dla zadania 7: "))
            k = int(input("Podaj drugą liczbę dla zadania 7: "))
            s = int(input("Podaj trzecią liczbę dla zadania 7: "))
            print(zadanie7(p, k, s))
    else:
        print("Podana liczba nie mieści się w zakresie od 1 do 7.")
except ValueError:
    print("To nie jest liczba od 1 do 7.")
