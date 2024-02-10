# Karta pracy nr 4

# Zadanie 1
def zadanie1(algorytm, a, b=None, wiek=None, waga=None, n=None):
    if algorytm == 1:
        return algorytm1(a, b)
    elif algorytm == 2:
        return algorytm2(a, b)
    elif algorytm == 3:
        return algorytm3(wiek)
    elif algorytm == 4:
        return algorytm4(waga)
    elif algorytm == 5:
        return algorytm5(n)
    else:
        return "Podano złą wartość."

def algorytm1(a, b) -> int:
    return a**2 + b**2

def algorytm2(a, b) -> int:
    return (a + b)**2

def algorytm3(wiek) -> str:
    if wiek >= 18:
        return "TAK"
    else:
        return "NIE"

def algorytm4(waga) -> str:
    if waga <= 20:
        return "TAK"
    else:
        return "NIE"

def algorytm5(n) -> list:
    fib = [1, 2]
    for i in range(2, n):
        next_term = fib[i - 1] + fib[i - 2]
        fib.append(next_term)
    return fib

# Zadanie 2
def zadanie2(n) -> int:
    cyfry = str(n)
    suma = sum([int(i) for i in cyfry])
    return suma

try:
    numer = int(input("Podaj numer zadania od 1 do 7: "))
    if 1 <= numer <= 7:
        if numer == 1:
            algorytm = int(input("Podaj który algorytm chcesz wykonać (1-5): "))
            if 1 <= algorytm <= 5:
                if algorytm in [1, 2]:
                    a = int(input("Podaj a: "))
                    b = int(input("Podaj b: "))
                    print(zadanie1(algorytm, a, b))
                elif algorytm in [3, 4]:
                    param = int(input(f"Podaj parametr: "))
                    print(zadanie1(algorytm, param))
                elif algorytm == 5:
                    n = int(input("Podaj n: "))
                    print(zadanie1(algorytm, n=n))
            else:
                print("Podano złą wartość.")
        elif numer == 2:
            n = int(input("Podaj liczbę: "))
            print(zadanie2(n))
    else:
        print("Podana liczba nie mieści się w zakresie od 1 do 7.")

except ValueError:
    print("Podano nieprawidłowe dane.")