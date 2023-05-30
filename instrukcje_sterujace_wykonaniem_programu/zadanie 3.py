import random

liczba = random.randint(0, 1000)
zgadnij = int(input("Spróbuj zgadnąć liczbę wylosowaną przez komputer: "))
petla = True
while petla:
    if zgadnij > liczba:
         print("wylosowana liczba jest mniejsza!")
         zgadnij = int(input("Spróbuj jeszcze raz: "))
    elif zgadnij < liczba:
        print("Wylosowana liczba jest większa!")
        zgadnij = int(input("Spróbuj jeszcze raz!: "))
    elif zgadnij == liczba:
            print("Tak!! udało ci się!!1")
            decyzja = input("Czy chcesz zagrać ponownie? t/n: ")
            decyzja = decyzja.lower()
            if decyzja == "t" or decyzja == "tak":
                 liczba = random.randint(0, 1000)
                 zgadnij = int(input("Spróbuj zgadnąć liczbę wylosowaną przez komputer: "))
                 continue
            else:
                petla = False

