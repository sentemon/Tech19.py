# Przestępność
# Mamy dany rok . Powiemy, że rok  jest przestępny, gdy wartość  jest podzielna przez 4. 
# Jeśli jednak wartość  dzieli się przez 100, a nie dzieli się przez 400 to rok  nie jest przestępny.

r = int(input())

if (r % 4 == 0 and r % 100 != 0) or (r % 400 == 0):
    print("TAK")
else:
    print("NIE")