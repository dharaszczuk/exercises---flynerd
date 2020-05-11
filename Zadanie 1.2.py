#kalkulator dziennego zapotrzebowania kalorycznego
w = float(input("Podaj swoją wagę w kilogramach: "))
h = float(input("Podajswój wzrost w centymetrach: "))
a = float(input("Podaj swój wiek: "))
s = str(input("Podadaj płeć k/m: "))

if s == "k":
    s = float(-161)
else:
    s = float(5) #stop kiedy s rózne od k lub m (?)
       
typ = {"1":1.2, "2":1.4, "3":1.6, "4":1.8, "5":2.0}
print("\nRodzaje aktywności fizycznej:")

print("1 - Praca siedząca, brak dodatkowej aktywności  zycznej")
print("2 - Praca nie zyczna, mało aktywny tryb życia")
print("3 - Lekka praca  zyczna,  regularne ćwiczenia 3-4 razy (ok. 5h) w tygodniu")
print("4 - Praca  zyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu")
print("5 - Praca  zyczna ciężka, regularne ćwiczenia 7razy w tygodniu")
t = input("Wybierz najlepiej pasujący rodzaj aktywności fizycznej: ")
activ = float(typ[t])
PPM = activ*(10 * w + 6.25 * h - 5 * a + s)
print("\nTwoje dzienne zapotrzebowanie kaloryczne wynosi: ", round(PPM, 1), "kcal")
