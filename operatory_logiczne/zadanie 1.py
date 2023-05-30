wiek = int(input("Podaj swój wiek kandydacie: "))

kategoria = input("Czy masz kategorię A2? tak/nie: ")
kategoria = kategoria.lower()

if kategoria == "tak":
    okres = int(input("jak długo masz kategorią A2? w latach: "))

wynik = False

if wiek == 20 and kategoria == "tak" and okres >= 2:
    wynik = True
elif wiek >= 24:
    wynik = True

if wynik == True:
    print("możesz zrobić prawko")
else: print("nie możesz zrobić prawka")
