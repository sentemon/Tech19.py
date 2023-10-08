# Karta pracy nr 2a

# Zadanie 1
def zadanie1(a, b):
    suma = a + b
    if suma % 2 == 0:
        return "TAK"
    else:
        return "NIE"

# Zadanie 2
def zadanie2(a, g):
    srednia_arytmetyczna = (a + g) / 2
    srednia_geometryczna = (a * g) ** 0.5

    if srednia_arytmetyczna > srednia_geometryczna:
        return "TAK"
    else:
        return "NIE"

# Zadanie 3
def zadanie3(k, l, m):
    if k == l and l != m:
        return "TAK, k i l są równe"
    elif k == m and k != l:
        return "TAK, k i m są równe"
    elif l == m and l != k:
        return "TAK, l i m są równe"
    else:
        return "NIE"

# Zadanie 4
def zadanie4(a, b, c, d):
    najmniejsza = min(a, b, c, d)
    return "Najmniejsza liczba: ", najmniejsza

# Zadanie 5
def zadanie5(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "TAK"
    else:
        return "NIE"

# Zadanie 6
def zadanie6(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "prostokątny"
        elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
            return "rozwartokątny"
        else:
            return "ostrokątny"
    else:
        return "Nie da się zbudować trójkąta."

try:
    numer_zadania = int(input("Podaj numer zadania od 1 do 6: "))
    if numer_zadania == 1:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print(zadanie1(a, b))
    elif numer_zadania == 2:
        a = float(input("Podaj pierwszą liczbę: "))
        g = float(input("Podaj drugą liczbę: "))
        print(zadanie2(a, g))
    elif numer_zadania == 3:
        k = int(input("Podaj pierwszą liczbę całkowitą: "))
        l = int(input("Podaj drugą liczbę całkowitą: "))
        m = int(input("Podaj trzecią liczbę całkowitą: "))
        print(zadanie3(k, l, m))
    elif numer_zadania == 4:
        a = int(input("Podaj pierwszą liczbę całkowitą: "))
        b = int(input("Podaj drugą liczbę całkowitą: "))
        c = int(input("Podaj trzecią liczbę całkowitą: "))
        d = int(input("Podaj czwartą liczbę całkowitą: "))
        print(zadanie4(a, b, c, d))
    elif numer_zadania == 5:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        c = float(input("Podaj trzecią liczbę: "))
        print(zadanie5(a, b, c))
    elif numer_zadania == 6:
        a = float(input("Podaj pierwszą liczbę: "))
        b = float(input("Podaj drugą liczbę: "))
        c = float(input("Podaj trzecią liczbę: "))
        print(zadanie6(a, b, c))
    else:
        print("Podano nieprawidłowy numer zadania.")
except ValueError:
    print("Podano nieprawidłowe dane.")
