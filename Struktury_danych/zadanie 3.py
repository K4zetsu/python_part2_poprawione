natura = ["burak", "cukinia", "pomidor", "cytryna", "ananas", "papryka", "dynia"]

litera = input("Podaj jedną literę i zobaczymy czy jest coś dla ciebie na liście!: ")

for x in natura:
    if x.startswith(litera):
        print(x)
    else: continue