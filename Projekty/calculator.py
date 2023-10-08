# Pobieranie dwóch liczb od użytkownika
a = int(input('Wpisz pierwszą liczbę: '))
b = int(input('Wpisz drugą liczbę: '))

# Wybór operacji matematycznej
x = input('Wybierz operację (+, -, *, /): ')

# Funkcja kalkulatora
def calculator(a, b, operator):
    wynik = None  # Inicjalizacja zmiennej wynik

    # Sprawdzanie wybranej operacji i wykonywanie odpowiedniego obliczenia
    if operator == '+':
        wynik = a + b
    elif operator == '-':
        wynik = a - b
    elif operator == '*':
        wynik = a * b
    elif operator == '/':
        # Obsługa dzielenia przez zero
        if b == 0:
            print('Nie można dzielić przez zero.')
            return
        wynik = a / b
    else:
        print('Nieprawidłowa operacja. Wybierz spośród: +, -, *, /')
        return

    # Wyświetlanie wyniku
    print(f'{a} {operator} {b} = {wynik}')

# Wywołanie funkcji kalkulatora
calculator(a, b, x)
