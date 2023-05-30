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
        mod1.dodawanie()
    elif wybor == 2:
        mod1.odejmowanie()
    elif wybor == 3:
        mod1.mnozenie()
    elif wybor == 4:
# 'try' sprawdzający walidację danych przy wykonywaniu dzielenia - jeśli użytkownik wpisze '0' jako dzielnik
# program zgłosi ZeroDivisionError, który zostanie obsłużony poleceniami w segmencie 'except' czyli wyświetli stosowny komunikat i przejdzie
# do następnej iteracji pętli
        try:
            mod1.dzielenie()
        except ZeroDivisionError:
            print("Nie możesz dzielić przez 0...")
            continue
# W przypadku wyboru opcji '0' wyświetlany jest stosowny komunikat, pętla zostaje przerwana i wykonanie programu konczy się
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break