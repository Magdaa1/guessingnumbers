import random
import math
import sys


class PoziomTrudnosci:
    """Klasa definiująca parametry poziomu trudności."""

    def __init__(self, nazwa, zakres, max_prob, podpowiedzi):
        self.nazwa = nazwa
        self.dolny_limit = 1
        self.gorny_limit = zakres
        self.max_prob = max_prob
        self.podpowiedzi = podpowiedzi  # Czy dostępne podpowiedzi

    def oblicz_optymalne_proby(self):
        """Oblicza teoretyczną liczbę prób (logarytm binarny)."""
        return math.ceil(math.log2(self.gorny_limit))


# Definicja poziomów
POZIOMY = {
    '1': PoziomTrudnosci('ŁATWY', 50, 10, True),
    '2': PoziomTrudnosci('ŚREDNI', 100, 7, True),
    '3': PoziomTrudnosci('TRUDNY', 500, 9, False),
    '4': PoziomTrudnosci('EKSPERT', 1000, 10, False)
}


def wyswietl_menu():
    """Wyświetla menu wyboru poziomu."""
    print("\n" + "=" * 50)
    print("🎲  GRA ZGADYWANIE LICZB  🎲".center(50))
    print("=" * 50)
    print("\nWybierz poziom trudności:\n")

    for klucz, poziom in POZIOMY.items():
        opt_proby = poziom.oblicz_optymalne_proby()
        podpowiedzi_tekst = "✓" if poziom.podpowiedzi else "✗"
        print(f"  [{klucz}] {poziom.nazwa:10} - Zakres: 1-{poziom.gorny_limit:4} | "
              f"Próby: {poziom.max_prob:2} | Podpowiedzi: {podpowiedzi_tekst} | "
              f"Optymalna strategia: {opt_proby} prób")

    print("\n  [Q] Wyjście")
    print("=" * 50)


def wybierz_poziom():
    """Pozwala graczowi wybrać poziom trudności."""
    while True:
        wyswietl_menu()
        wybor = input("\nTwój wybór: ").strip().upper()

        if wybor == 'Q':
            print("Do zobaczenia!")
            return None

        if wybor in POZIOMY:
            return POZIOMY[wybor]

        print("❌ Nieprawidłowy wybór! Spróbuj ponownie.")


def podaj_podpowiedz(wylosowana, proby, poziom):
    """Generuje podpowiedź w zależności od liczby prób."""

    if not poziom.podpowiedzi:
        return None

    # Progresywne podpowiedzi
    if proby == poziom.max_prob - 3:
        if wylosowana % 2 == 0:
            return "💡 Podpowiedź: Liczba jest PARZYSTA"
        else:
            return "💡 Podpowiedź: Liczba jest NIEPARZYSTA"

    elif proby == poziom.max_prob - 1:
        # Podaj przedział
        polowa = poziom.gorny_limit // 2
        if wylosowana <= polowa:
            return f"💡 Podpowiedź: Liczba jest w zakresie 1-{polowa}"
        else:
            return f"💡 Podpowiedź: Liczba jest w zakresie {polowa + 1}-{poziom.gorny_limit}"

    return None


def gra_zgadywanie_liczb():
    """Główna funkcja gry z systemem poziomów."""

    # Wybór poziomu
    poziom = wybierz_poziom()
    if poziom is None:
        return

    # Inicjalizacja gry
    wylosowana_liczba = random.randint(poziom.dolny_limit, poziom.gorny_limit)
    proby = 0
    historia = []  # Lista poprzednich zgadnięć

    print(f"\n🎯 Poziom: {poziom.nazwa}")
    print(f"Zakres: {poziom.dolny_limit}-{poziom.gorny_limit}")
    print(f"Maksymalna liczba prób: {poziom.max_prob}")
    print(f"Optymalna strategia: {poziom.oblicz_optymalne_proby()} prób (przeszukiwanie binarne)\n")

    try:
        while proby < poziom.max_prob:
            # Pokaż pozostałe próby
            pozostalo = poziom.max_prob - proby
            print(f"[Próba {proby + 1}/{poziom.max_prob}] Pozostało: {pozostalo}")

            # Pokaż historię (ostatnie 3 próby)
            if historia:
                ostatnie = historia[-3:]
                print(f"  Twoje poprzednie próby: {', '.join(map(str, ostatnie))}")

            # Podpowiedź (jeśli dostępna)
            podpowiedz = podaj_podpowiedz(wylosowana_liczba, proby, poziom)
            if podpowiedz:
                print(f"  {podpowiedz}")

            # Pobierz liczbę
            zgadywana_str = input("Podaj swoją liczbę: ")

            # Walidacja
            try:
                zgadywana = int(zgadywana_str)
            except ValueError:
                print("To nie jest prawidłowa liczba!\n")
                continue

            if zgadywana < poziom.dolny_limit or zgadywana > poziom.gorny_limit:
                print(f"Liczba musi być w zakresie {poziom.dolny_limit}-{poziom.gorny_limit}!\n")
                continue

            # Zwiększ licznik i dodaj do historii
            proby += 1
            historia.append(zgadywana)

            # Sprawdź odpowiedź
            if zgadywana < wylosowana_liczba:
                roznica = wylosowana_liczba - zgadywana
                if roznica <= 5:
                    print("Ciepło! Za mało!\n")
                else:
                    print("Za mało!\n")

            elif zgadywana > wylosowana_liczba:
                roznica = zgadywana - wylosowana_liczba
                if roznica <= 5:
                    print("Ciepło! Za dużo!\n")
                else:
                    print("Za dużo!\n")

            else:
                # WYGRANA!
                print(f"GRATULACJE! Odgadłeś liczbę {wylosowana_liczba}!")
                print(f"Liczba prób: {proby}/{poziom.max_prob}")

                # Ocena wydajności
                optymalna = poziom.oblicz_optymalne_proby()
                if proby <= optymalna:
                    print("PERFEKCYJNIE! Osiągnąłeś optymalny wynik!")
                elif proby <= poziom.max_prob // 2:
                    print("ŚWIETNIE! Powyżej średniej!")
                else:
                    print("DOBRZE! Udało się!")
                return

        # PRZEGRANA (zabrakło prób)
        print("\n" + "😞" * 25)
        print(f"Niestety przegrałeś! Zabrakło prób.")
        print(f"Prawidłowa liczba to: {wylosowana_liczba}")
        print(f"Twoje próby: {', '.join(map(str, historia))}")
        print("😞" * 25)

    except KeyboardInterrupt:
        print("\n\nGra przerwana przez użytkownika. Do zobaczenia!")

def main():
    """Główna pętla programu z możliwością ponownej gry."""
    try:
        while True:
            gra_zgadywanie_liczb()

            print("\n" + "=" * 50)
            try:
                ponownie = input("Chcesz zagrać ponownie? (T/N): ").strip().upper()
            except KeyboardInterrupt:
                print("\n\nProgram zostal zamkniety.")
                break
            if ponownie != 'T':
                print("\nDziękuję za grę! Do zobaczenia!")
                break
    except KeyboardInterrupt:
        # Dodatkowa ochrona (gdyby coś przeszło przez pierwszy try-except)
        print("\n\n⚠️ Program zakończony (Ctrl+C/Stop). Do zobaczenia! 👋")

    except Exception as ex:
        # Łapie wszystkie inne nieoczekiwane błędy
        print(f"\n❌ Krytyczny błąd programu: {ex}")
        print("Program zostanie zamknięty.")
        sys.exit(1)

    finally:
        # Ten blok wykona się ZAWSZE, niezależnie od tego, jak zakończył się program
        print("\n" + "=" * 50)
        print("Program zakończony.".center(50))
        print("=" * 50)



if __name__ == "__main__":
    main()