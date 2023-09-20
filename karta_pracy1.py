# zadanie 1
def zadanie1(a, b):
    print(f"{a**2} + {b**2} = {a**2 + b**2}") 
# zadanie 2
def zadanie2(a, b):
    print(f"({a} + {b})^2 = {(a + b)**2}")
# zadanie 3
def zadanie3(a, b):
    print(f"({a} - {b})^3 = {(a - b)**3}")
# zadanie 4
def zadanie4(a, b, c):
    print(f"{a} * {b} * {c} = {a * b * c}")
# zadanie 5
def zadanie5(a, b):
    print(f"({a} + {b}) * 0.4 = {(a + b) * 0.4}")
# zadanie 6
def zadanie6(brutto):
    print(f"{brutto} / 1.23 = {brutto / 1.23}")
# zadanie 7
def zadanie7(a, b):
    print(f"{a} % {b} = {a % b}")

# Prośba o podanie liczby od 1 do 7
try:
    numer = int(input("Podaj liczbę od 1 do 7: "))
    if 1 <= numer <= 7:
        # Wywołanie odpowiedniej funkcji na podstawie wybranej liczby
        if numer == 1:
            a = float(input("Podaj pierwszą liczbę a: "))
            b = float(input("Podaj drugą liczbę b: "))
            zadanie1(a, b)
        elif numer == 2:
            a = float(input("Podaj pierwszą liczbę a: "))
            b = float(input("Podaj drugą liczbę b: "))
            zadanie2(a, b)
        elif numer == 3:
            a = float(input("Podaj pierwszą liczbę a: "))
            b = float(input("Podaj drugą liczbę b: "))
            zadanie3(a, b)
        elif numer == 4:
            a = float(input("Podaj pierwszą liczbę a: "))
            b = float(input("Podaj drugą liczbę b: "))
            c = float(input("Podaj trzecią liczbę c: "))
            zadanie4(a, b, c)
        elif numer == 5:
            a = float(input("Podaj pierwszą liczbę a: "))
            b = float(input("Podaj drugą liczbę b: "))
            zadanie5(a, b)
        elif numer == 6:
            brutto = float(input("Podaj wartość brutto: "))
            zadanie6(brutto)
        elif numer == 7:
            a = float(input("Podaj pierwszą liczbę a: "))
            b = float(input("Podaj drugą liczbę b: "))
            zadanie7(a, b)
    else:
        print("Podana liczba nie mieści się w zakresie od 1 do 7.")
except ValueError:
    print("To nie jest liczba od 1 do 7.")
