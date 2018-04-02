while True:
    def cel_to_fah():
        sonuc2 = ((cel*9) / 5) + 32
        return sonuc2
    def cel_to_kel():
        sonuc3 = cel+273
        return sonuc3
    def cel_to_rea():
        sonuc4 = ((cel+273)*9)/5
        return sonuc4
    def rea_to_fah():
        sonuc5 = (rea-459.69)
        return sonuc5
    def rea_to_cel():
        sonuc7 = ((rea-491.69)*5)/9
        return sonuc7
    def rea_to_kel():
        sonuc8 = ((rea)*5)/9
        return sonuc8
    def fah_to_rea():
        sonuc10 = fah+459.69
        return sonuc10
    def fah_to_cel():
        sonuc11 = ((fah-32)*5)/9
        return sonuc11
    def fah_to_kel():
        sonuc12 = (((fah-32)*5)/9)+273
        return sonuc12
    def kel_to_fah():
        sonuc14 = (((kel-273)*9)/5)+32
        return sonuc14
    def kel_to_rea():
        sonuc15 = (kel*9)/5
        return sonuc15
    def kel_to_cel():
        sonuc16 = (kel-273)
        return sonuc16
    print("""Celcius    (1)
             Kelvin     (2)
             Fahrenheit (3)
             Rankin     (4)
             --------------""")
    mesaj1 = input("Hangi birimi donusturmek istiyorsunuz? : ")

    if mesaj1=="1":
        cel=input("Celcius degerini girin : ")
        print("%s celcius, %s kelvin'e esittir.".format(cel, cel_to_kel()))
        print("%s celcius, %s fahrenheit'e esittir.".format(cel, cel_to_fah()))
        print("%s celcius, %s rankin'e esittir.".format(cel, cel_to_rea()))
        print
    elif mesaj1=="2":
        kel=input("Kelvin degerini girin : ")
        print "%s kelvin, %s celcius'a esittir." %(kel, kel_to_cel())
        print "%s kelvin, %s fahrenheit'e esittir." %(kel, kel_to_fah())
        print "%s kelvin, %s rankin'e esittir." %(kel, kel_to_rea())
        print
    elif mesaj1=="3":
        fah=input("Fahrenheit degerini girin : ")
        print "%s fahrenheit, %s celcius'a esittir." %(fah, fah_to_cel())
        print "%s fahrenheit, %s kelvin'e esittir." %(fah, fah_to_kel())
        print "%s fahrenheit, %s rankin'e esittir." %(fah, fah_to_rea())
        print
    elif mesaj1=="4":
        rea=input("Rankin degerini girin : ")
        print "%s rankin, %s celcius'a esittir." %(rea, rea_to_cel())
        print "%s rankin, %s kelvin'e esittir." %(rea, rea_to_kel())
        print "%s rankin, %s fahrenheit'e esittir." %(rea, rea_to_fah())
        print
    else:
        print ("Islem numarasi gecersiz. Program sonlandirilacak.")
        break
