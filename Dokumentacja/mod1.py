
# Jest to plik z funkcjami konkretnych działań, które będziemy wywoływać, w każdej funkcji pobierane są 2 wartości od użytkownika a następnie wykonywane są stosowne polecenia
def dodawanie(a: int, b: int) -> int:
    return a + b

def odejmowanie(a : int, b: int) -> int:
    return a - b

def mnozenie(a: int, b: int):
    return a * b
# W przypadku dzielenia moglibyśmy dodać tutaj prostą walidację danych, nie jest to konieczne ponieważ jest ona zawarta w pliku glównym.
# Poza tym jest problem polegający na tym, że nie jesteśmy w stanie w funkcji użyć potrzebnego polecenia 'continue' przechodzącego
# do następnej iteracji pętli. Problem ten znika, gdy walidacja znajduje się w pliku głównym.
# Warto też wspomnieć, że wynik w tym wypadku będzie typem 'float' a nie 'int'. Python automatycznie konwertuje typ danych na 'float'
# zakładając, że wynik może zawierać jakąś resztę z dzielenia. Aby tego uniknąć musielibyśmy zamienić ponownie typ 'float' na 'int' jednak wynik
# byłby niedokładny.
def dzielenie(a: float, b: float) -> float:
    return a / b
    
