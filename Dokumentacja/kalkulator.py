#import odpowiedniego, wcześniej utworzonego pliku z metodami
import mod1
#Początek pętli kalkulatora
while True:
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("0. koniec")
#Wybór działania, które chcemy wykonać 
    wybor = int(input("Którą operację chcesz wykonać?: "))
#warunek 'if' sprawdzający, którą opcję wybrał użytkownik
    if wybor == 1:
#tutaj jak i w pozostałych opcjach, wywołanie odpowiedniej funkcji z zaimportowanego pliku
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print(f"Wynik dodawania {a} + {b} to : {mod1.dodawanie(a, b)}")
    elif wybor == 2:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print(f"Wynik odejmowania {a} - {b} to : {mod1.odejmowanie(a, b)}")
    elif wybor == 3:
        a = int(input("Podaj pierwszą liczbę: "))
        b = int(input("Podaj drugą liczbę: "))
        print(f"Wynik mnożenia {a} * {b} to : {mod1.mnozenie(a, b)}")
    elif wybor == 4:
# 'try' sprawdzający walidację danych przy wykonywaniu dzielenia - jeśli użytkownik wpisze '0' jako dzielnik
# program zgłosi ZeroDivisionError, który zostanie obsłużony poleceniami w segmencie 'except' czyli wyświetli stosowny komunikat i przejdzie
# do następnej iteracji pętli
        try:
            a = int(input("Podaj pierwszą liczbę: "))
            b = int(input("Podaj drugą liczbę: "))
            print(f"Wynik dzielenia {a} / {b} to : {mod1.dzielenie(a, b)}")
        except ZeroDivisionError:
            print("Nie możesz dzielić przez 0...")
            continue
# W przypadku wyboru opcji '0' wyświetlany jest stosowny komunikat, pętla zostaje przerwana i wykonanie programu konczy się
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break