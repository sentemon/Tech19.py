a, b = int(input('wpisz pierwwsza liczbe')), int(input('wpisz druga liczbe'))
x = input(3
          'wpisz operqacje: +, -, *, /')
def kalkulator(a, b):
  if x == '+':
    print(f'{a} + {b} = {a + b}')
  elif x == '-':
    print(f'{a} - {b} = {a - b}')
  elif x == '*':
    print(f'{a} * {b} = {a * b}')
  elif x == '/':
    print(f'{a} / {b} = {a / b}')
kalkulator(a, b)