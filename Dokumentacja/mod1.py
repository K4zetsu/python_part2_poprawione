
# Jest to plik z funkcjami konkretnych działań, które będziemy wywoływać, w każdej funkcji pobierane są 2 wartości od użytkownika a następnie wykonywane są stosowne polecenia
def dodawanie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = a + b
    print(a, "+", b, "=", wynik)

def odejmowanie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = a - b
    print(a, "-", b, "=", wynik)

def mnozenie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = a * b
    print(a, "*", b, "=", wynik)
# W przypadku dzielenia moglibyśmy dodać tutaj prostą walidację danych, nie jest to konieczne ponieważ jest ona zawarta w pliku glównym.
# Poza tym jest problem polegający na tym, że nie jesteśmy w stanie w funkcji użyć potrzebnego polecenia 'continue' przechodzącego
# do następnej iteracji pętli. Problem ten znika, gdy walidacja znajduje się w pliku głównym.
# Warto też wspomnieć, że wynik w tym wypadku będzie typem 'float' a nie 'int'. Python automatycznie konwertuje typ danych na 'float'
# zakładając, że wynik może zawierać jakąś resztę z dzielenia. Aby tego uniknąć musielibyśmy zamienić ponownie typ 'float' na 'int' jednak wynik
# byłby niedokładny.
def dzielenie():
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj drugą liczbę: "))
    wynik = a / b
    print(a, ":", b, "=", wynik)
