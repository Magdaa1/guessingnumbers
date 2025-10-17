#1. Ustal zakres liczb jaie beda uzywane
#2. Wylosuj tajna liczbe
#3. Ustawienie zmiennej do sledzneia prob
import random

def gra_zgadywanie_liczb():
    dolny_limit = 1
    gorny_limit = 100

    wylosowana_liczba = random.randint(dolny_limit, gorny_limit)
    proby = 0

    print("Witaj w grze Zgadywanie Liczb! Sprobuj odgadnac wylosowana liczbe {dolny_limit} i {gorny_limit}. \n" )


#1. Popros gracza o podanie zgadywanej liczby
#2. sprawdz obsluge bledow np poda jakas litere zamiast cyfry
#3. sprawdz, czy liczba jest w zakresie i zwieksz liczbe prob
#4 porownianie czy liczba jest za duza czy za mala


    while True:
        zgadywana_liczba_str = input("Podaj swoja liczbe:")
        try:
            zgadywana_liczba = int(zgadywana_liczba_str)
        except ValueError:
            print(f"To nie jest prawidlowa liczba. Sprobuj ponownie.")
            continue

        if zgadywana_liczba < dolny_limit or zgadywana_liczba > gorny_limit:
            print(f"Liczba musi byc w zakresie od {dolny_limit} do {gorny_limit}. Sprobuj pownownie")
            proby -= 1
            continue
        proby += 1

        if zgadywana_liczba < wylosowana_liczba:
            print("Za malo! ")
        elif zgadywana_liczba > wylosowana_liczba:
            print("Za duzo! ")
        else:
            print(f"Gratulacje! Odgadles liczbe {wylosowana_liczba} w {proby} probach")
            break
if __name__ == "__main__":
    gra_zgadywanie_liczb()

