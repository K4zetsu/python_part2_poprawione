import mod1

while True:
    print("1. dodawanie")
    print("2. odejmowanie")
    print("3. mnożenie")
    print("4. dzielenie")
    print("0. koniec")

    wybor = int(input("Którą operację chcesz wykonać?: "))

    if wybor == 1:
        mod1.dodawanie()
    elif wybor == 2:
        mod1.odejmowanie()
    elif wybor == 3:
        mod1.mnozenie()
    elif wybor == 4:
        try:
            mod1.dzielenie()
        except ZeroDivisionError:
            print("Nie możesz dzielić przez 0...")
            continue
    elif wybor == 0:
        print("Dziękuję za korzystanie z naszych usług!!")
        break