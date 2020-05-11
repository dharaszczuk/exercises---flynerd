#kalkulator BMI
h = float(input("Podaj swój wzrost w metrach: "))
w = float(input("Podaj swoją wagę w kilogramach: "))
BMI = w/(h**2)
print ("Twoje BMI wynosi: ", round(BMI, 2))
