import random


def gra_zgadywanie_liczb():
    """Gra w zgadywanie liczb z zakresu 1-100."""

    dolny_limit = 1
    gorny_limit = 100

    wylosowana_liczba = random.randint(dolny_limit, gorny_limit)

    proby = 0

    print(f"Witaj w grze Zgadywanie Liczb!")
    print(f"Spróbuj odgadnąć wylosowaną liczbę z zakresu {dolny_limit} i {gorny_limit}.\n")

    try:
        while True:
            zgadywana_liczba_str = input("Podaj swoją liczbę: ")

            try:
                zgadywana_liczba = int(zgadywana_liczba_str)
            except ValueError:
                print("To nie jest prawidłowa liczba. Spróbuj ponownie.\n")
                continue  # Wróć na początek pętli

            # 3. Sprawdź, czy liczba jest w zakresie
            if zgadywana_liczba < dolny_limit or zgadywana_liczba > gorny_limit:
                print(f"Liczba musi być w zakresie od {dolny_limit} do {gorny_limit}. Spróbuj ponownie.\n")
                continue  # Wróć na początek pętli

            # Zwiększ liczbę prób (tylko dla poprawnych liczb)
            proby += 1

            # 4. Porównanie czy liczba jest za duża czy za mała
            if zgadywana_liczba < wylosowana_liczba:
                print("Za mało!\n")
            elif zgadywana_liczba > wylosowana_liczba:
                print("Za dużo!\n")
            else:
                print(
                    f"Gratulacje! Odgadłeś liczbę {wylosowana_liczba} w {proby} {'próbie' if proby == 1 else 'próbach'}!")
                break  # Wyjdź z pętli

    except KeyboardInterrupt:
        print("\n\nGra przerwana przez użytkownika. Do zobaczenia!")


# Uruchomienie gry
if __name__ == "__main__":
    gra_zgadywanie_liczb()