def oblicz_pole_i_obwod(figura):
    if figura == "trójkąt":
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        c = float(input("Podaj długość boku c: "))
        pole = (a * b) / 2
        obwod = a + b + c
    elif figura == "kwadrat":
        a = float(input("Podaj długość boku a: "))
        pole = a ** 2
        obwod = 4 * a
    elif figura == "kolo":
        r = float(input("Podaj promień koła: "))
        pole = 3.14 * r**2
        obwod = 2 * 3.14 * r
    elif figura == "prostokąt":
        a = float(input("Podaj długość boku a: "))
        b = float(input("Podaj długość boku b: "))
        pole = a * b
        obwod = 2 * (a + b)
    elif figura == "trapez":
        a = float(input("Podaj długość podstawy a: "))
        b = float(input("Podaj długość podstawy b: "))
        h = float(input("Podaj wysokość trapezu: "))
        pole = (a + b) * h / 2
        obwod = a + b + 2 * (h**2 + ((b - a) / 2)**2)**0.5
    elif figura == "romb":
        d1 = float(input("Podaj długość pierwszej przekątnej: "))
        d2 = float(input("Podaj długość drugiej przekątnej: "))
        pole = (d1 * d2) / 2
        obwod = 4 * (d1**2 + d2**2)**0.5
    else:
        print("Nieznana figura.")
        return

    print(f"Pole {figura} wynosi: {pole}")
    print(f"Obwód {figura} wynosi: {obwod}")

try:
    figura = input("Podaj figurę (trójkąt, kwadrat, kolo, prostokąt, trapez, romb): ")
    oblicz_pole_i_obwod(figura)
except ValueError:
    print("Błędne dane wejściowe.")
