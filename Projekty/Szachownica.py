# Szachownica
# Napisz program, który dla podanej na standardowym wejściu liczby całkowitej n, narysuje szachownicę z cyfr 0 i 1 o boku n

n = int(input())

for i in range(n):
    row = [str((i + j) % 2) for j in range(n)]
    print("".join(row))