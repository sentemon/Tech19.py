# Karta Pracy nr 2
# zadanie 1
a1 = int(input())
if a1 % 3 == 0:
    print("TAK")
else:
    print("NIE")
# zadanie 2
a2 = int(input())
if len(str(a2)) == 3 and a2 % 17 == 0:
    print("TAK")
else:
    print("NIE")

# zadanie 3
yo = int(input())
if yo >= 18:
    print("TAK")
else:
    print("NIE")

# zadanie 4
waga = int(input())
limit = 20
if waga <= limit:
    print("TAK")
else:
    print("NIE")

# zadanie 5
a, b, c = int(input()), int(input()), int(input())
if (a < c and b > c) or (b < c and a > c):
    print("TAK")
else:
    print("NIE")

# zadanie 6

a, p = int(input()), int(input())
if ((a**p - a) % p == 0):
    print("TAK")
else:
    print("NIE")

# zadanie 7
p, k, s = int(input()), int(input()), int(input())
if p + 3 * s >= k:
    print("TAK")
else:
    print("NIE")
