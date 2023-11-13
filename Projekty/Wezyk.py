# Wężyk
# Na wyjście należy wypisać n wierszy, w każdym z nich po n liczb naturalnych. Razem ma zostać wypisanych n^2 liczb: wszystkie liczby naturalne od 1 do n^2 .
# W każdym wierszu wypisane liczby powinny być pooddzielane pojedynczymi odstępami.

n = int(input())

for i in range(1, n*n+1, n):
    wez = list(range(i, i + n))
    if i // n % 2 == 1:
        wez.reverse()
    print(*wez)