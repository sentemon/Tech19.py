# Kraty pracy nr 3b

# zadanie 1
def zadanie1():
    for i in range(1, 31):
        print(i)

# zadanie 2
def zadanie2(n):
    for i in range(1, n+1, 2):
        print(i**2)

# zadanie 3
def zadanie3():
    for i in range(1137, 10000, 379):
        print(i)

# zadanie 4
def zadanie4():
    for i in range(100, 1000):
        if i % 5 == 0 or i % 6 == 0 or i % 11 == 0:
            print(i)

# zadanie 5
def zadanie5():
    suma = 0
    n = int(input())
    for i in range(n):
        num = int(input())
        suma += n
    print(suma)

# zadanie 6
def zadanie6():
    k = int(input())
    suma = 0
    for i in range(2, k+1, 2):
        suma += i
    print(suma)

# zadanie 7
def zadanie7():
    m = int(input())
    suma = 0
    for i in range(11, m+1, 2):
        suma += i
    print(suma)

