a, b = int(input('Wpisz pierwszą liczbę')), int(input('Wpisz drugą liczbę')) #kalkulator
x = input('Wybierz operacje: (+, -, *, /)')
def calculator(a, b):
  if x == '+':
    print(f'{a} + {b} = {a + b}')
  elif x == '-':
    print(f'{a} - {b} = {a - b}')
  elif x == '*':
    print(f'{a} * {b} = {a * b}')
  elif x == '/':
    print(f'{a} / {b} = {a / b}')
calculator(a, b)
