# FOR 

# Napisz program wyświetlający liczby całkowite z przedziału <1,20> 
liczby = [i for i in range(1, 21)]
print(*liczby)

# Napisz program wyświetlający liczby całkowite z przedziału <100,50> w porządku  
liczby = [i for i in range(100, 49, -1)]
print(*liczby)

# Napisz program wyświetlający liczby całkowite (co 5) z przedziału <5,10,15,20 … 100>malejącym. 
liczby = [i for i in range(100, 5, -5)]
print(*liczby)

# Napisz program wyświetlający liczby całkowite z przedziału <0,y> (wartość y podaje użytkownik) 
liczby = [i for i in range(0, int(input()))]
print(*liczby)

# Napisz program wyświetlający liczby całkowite z przedziału <x,y> (wartości x i y podaje użytkownik) 
liczby = [i for i in range(int(input()), int(input()) + 1)]
print(*liczby)




# WHILE 

# Napisz program wyświetlający liczby całkowite z przedziału <1,20> 
i = 1
while i <= 20:
  print(i, end=" ")
  i+=1

# Napisz program wyświetlający liczby całkowite z przedziału <100,50> w porządku malejącym. 
i = 100
while i >= 50:
  print(i, end=" ")
  i-=1

# Napisz program wyświetlający liczby całkowite z przedziału <5,10,15,20 … 100>
i = 5
while i <= 100:
  print(i, end=" ")
  i+=5

# Napisz program wyświetlający liczby całkowite z przedziału <0,y> (wartość y podaje użytkownik)
x = 0
y = int(input())
while x <= y:
  print(x, end=" ")
  x+=1

# Napisz program wyświetlający liczby całkowite z przedziału <x,y> (wartości x i y podaje użytkownik)
x = int(input())
y = int(input())
while x <= y:
  print(x, end=" ")
  x+=1