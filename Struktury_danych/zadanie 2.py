slowo = input("Wpisz jakieś słowo i sprawdzimy czy to ten paralidndrom: ")

if slowo[::] == slowo[::-1]:
    print("tak to jest paralindrom!")
else:
     print("to nie jest paralindromum!")