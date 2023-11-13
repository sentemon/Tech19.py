# Zadanie 8WST – Wstawianie liczb
# Dane jest 10 liczb. Wstaw pierwszą liczbę przed najwcześniejszą większą od niej.

numbers = list(map(int, input().split()))

pierwsza = numbers[0]

for i, x in enumerate(numbers):
    if x > pierwsza:
        indeks_wiekszej = i
        break

result = numbers[:indeks_wiekszej] + [pierwsza] + numbers[indeks_wiekszej:]

print(*result[1:])