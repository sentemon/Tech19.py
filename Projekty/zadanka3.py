# zadanka 3
# zadanie 1
n = int(input())

if (n % 2 == 0):
    print(f"liczba {n} jest parzysta")
else:
    print(f"liczba {n} jest nieparzysta")

# zadanie 2
a, b, c = int(input()), int(input()), int(input())
if a + b > c and a + c > b and b + c > a:
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print(f"trojkat o bokach {a}, {b}, {c} jest prostokat")
    else:
        print(f"trojkat o bokach {a}, {b}, {c} nie jest prostokątny")

# zadanie 3
n = int(input())
for i in range(n):
    print("powtótrzenie nr.", i)

# zadanie 4
n = int(input())
for i in range(1, n):
    if i % 3 == 0:
       print(i)

# zadanie 5
n = int(input())
my_list = []
for i in range(1, n):
    if n % i == 0:
      my_list.append(i)
if sum(my_list) == n:
    print(f"liczba {n} jest liczba doskonala")
else:
    print(f"liczba {n} nie jest liczba doskonala")

# # zadanie 6
n = int(input())
p = 3
if n == (2**p-1)*2**(p-1):
    print(f"liczba {n} jest liczba doskonala")
else:
    print(f"liczba {n} nie jest liczba doskonala")

# zadanie 7
flag = True
print("Jak się masz?")
while flag:
    s = input()
    if s != "OK":
      print("Jak się masz?")
    else:
      flag = False

# zadanie 8
n = int(input())
my_list = []
for i in range(2, n):
    if n % i == 0:
      my_list.append(i)
if len(my_list) > 0:
    print("ma", *my_list)
else:
    print("nie ma")
