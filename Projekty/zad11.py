from math import sqrt
a, b, c = int(input()), int(input()), int(input())

delta = b ** 2 - 4 * a * c
if delta < 0:
  x1 = -b + sqrt(-delta) / (2 * a)
  x2 = -b - sqrt(-delta) / (2 * a)
  print(x1, x2)
elif delta == 0:
  x1 = (-b / (2 * a))
  print(x1)
else:
  print("Brak pierwistków")