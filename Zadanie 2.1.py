"""Chcemy aby skrypt:
Zapytał o Twoje imię
Powitał Cię po imieniu
Zapytał o Twój wiek
Zapytał o peron z Harrego Potter’a
Odpowiedział (dowolnie łącząc wiek i peron), czy jest sens jechać do
Hogwartu """

name = input ("Podaj swoje imię: ")
print ("Cześć ", name, "ile masz lat?")
age = input ("Podaj swój wiek: ")
peron = input ("Z jakiego peronu odjeżdża pociąg do Hogwartu? ")
print ("\n", name, "nie uważasz, że mając ", age, "lat, nie ma już sensu jechać z peronu", peron, "do Hogwartu?!")
input ("Aby zakończyć wciśnij dowoly klawisz...")
