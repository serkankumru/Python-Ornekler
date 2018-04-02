#a = input("Adinizi Giriniz ")
#print("Adiniz " +a)
#print("birinci satır", "ikinci satır", "üçüncü satır", sep="\n")
#print("Serkan","Kumru","1997",sep = "\n")
#print("bir", "iki", "üç", "dört", "on dört",sep=" mumdur ", end=" mumdur\n")
#f = open("Deneme.txt","w")
#print("Adiniz Dosyaya Kayit Edildi \n"+a,file=f)
#f.close()
tum = """
-----------------------------------------------------------------
anahtar = 1
while anahtar == 1:
   print("Toplama-1\nCikarma-2\nCarpma--3\nBolme---4\nCikis---q")
    secim = input("\nSeciminiz :")
    
    if secim == "1":
        sayi1 = int(input("Sayi 1 :"))
        sayi2 = int(input("Sayi 2 :"))
        print(sayi1," + ",sayi2," = ",sayi1+sayi2)
    elif secim == "2":
        sayi1 = int(input("Sayi 1 :"))
        sayi2 = int(input("Sayi 2 :"))
        print(sayi1," - ",sayi2," = ",sayi1-sayi2)
    elif secim == "3":
        sayi1 = int(input("Sayi 1 :"))
        sayi2 = int(input("Sayi 2 :"))
        print(sayi1," * ",sayi2," = ",sayi1*sayi2)
    elif secim == "4":
        sayi1 = int(input("Sayi 1 :"))
        sayi2 = int(input("Sayi 2 :"))
        print(sayi1," / ",sayi2," = ",sayi1 / sayi2)
    elif secim == "q":
        print("Cikis islemi yapildi...")
        anahtar = 0
    else:
        print("Tekarar deneyin\n")
        sayi1 = int(input("Sayi 1 :"))
        sayi2 = int(input("Sayi 2 :"))
        hesap(sayi1,sayi2)
        
    
def hesap(a,n):
    print("a + n = ",a+n)

----------------------------------------------------------------
kelime = "Serkan"
a = input("Bir kaekter giriniz :")
al = eval(a)
if al in kelime:
    print("karekter kelimede var ")
--------------------------------------------------------------
while True:
    parola = input("Parolaniz :")
    if not parola:
        print("Parolaa Kismi bos gecilemez...")
    elif len(parola)>11:
        print("Parola 11 haneyi gecmemeli")
    else:
        print("Parolaniz Yenilendi Yeni parolaniz : ******"+parola[6:11])
        break
------------------------------------------------------------------------
f = open("Deneme.txt","r")
print(f.read())

f.close()
------------------------------------------------------------------------
try:
    f = open("Deneme.txt","r")
    print(f.read())
except IOError:
    print("Bir Hata Olustu...")
    quit()
finally:
    f.close()
------------------------------------------------------------------------
with open("Deneme.txt","r") as f:
    print(f.read())
------------------------------------------------------------------------
ozyinelemeli fonksiton

a = [1,2,3,4,5]
print(topla(a))

def topla(liste):
    if len(liste) == 0:
        return 0
    else:
        return liste[0]+topla(liste[1:])


-----------------------------------------------------------------------
f = open("kisiler.txt","w")
a = 0
while a < 3:
    kisiad=  input("Adinizi giriniz  :")
    telno = int(input("Telefonunuzu gir :"))
    print(kisiad,":",telno,file = f)
    a+=1
    
f.close()

f = open("kisiler.txt","r")
print("\n")
print(f.read())
------------------------------------------------------------------------
f = open("deneme.txt","w")
for a in range(100,10,-3):
    for b in range(10,100,3):
        if a == b:
            print(a," = ",b,file = f)
    
f.close()

f = open("deneme.txt")
print(f.read())
f.close()
-----------------------------------------------------------------------
asalmi = int(input("Bir Sayi Giriniz :"))
anahtar = 1
for a in range(2,asalmi):
    sonuc = asalmi % a
    if sonuc == 0:
        print("Sayi Asal Degildir...")
        anahtar = 0
        break
if anahtar == 1:
    print("Sayi Asal Sayidir...")
---------------------------------------------------------------------   
ilk_metin = "Serkan"
ikinci_metin = "Kumru"
fark = ''
for s in ikinci_metin:
    if not s in ilk_metin:
        if not s in fark:
            fark += s
print(fark)
---------------------------------------------------------------------
"""
metin = """Bu programlama dili Guido Van Rossum adlı Hollandalı bir programcı
tarafından 90’lı yılların başında geliştirilmeye başlanmıştır. Çoğu insan,
isminin Python olmasına aldanarak, bu programlama dilinin, adını piton
yılanından aldığını düşünür. Ancak zannedildiğinin aksine bu programlama dilinin
adı piton yılanından gelmez. Guido Van Rossum bu programlama dilini, The Monty
Python adlı bir İngiliz komedi grubunun, Monty Python’s Flying Circus adlı
gösterisinden esinlenerek adlandırmıştır. Ancak her ne kadar gerçek böyle olsa
da, Python programlama dilinin pek çok yerde bir yılan figürü ile temsil
edilmesi neredeyse bir gelenek halini almıştır."""
"""
---------------------------------------------------------------------
say = 0
harf = input("Metinde Aranacak Harfi Giriniz :")
for a in metin:
    if a == harf:
        print(a)
        say += 1
    
print("Bu metinde",say,"Tane",harf,"Karekterinden Var.")
--------------------------------------------------------------------
f = open("AC.txt","w")
for a in metin:
    f.write(a)

f.close()
f = open("AC.txt","w")
x = f.seek(34)
print(x)
f.close()
--------------------------------------------------------------------
for a in metin:
    if a <= 'A':
        if a >= 'Z':
            print(a)
--------------------------------------------------------------------
ata1 = "Akıllı bizi arayıp sormaz deli bacadan akar!"
ata2 = "Ağa güçlü olunca kul suçlu olur!"
ata3 = "Avcı ne kadar hile bilirse ayı da o kadar yol bilir!"
ata4 = "Lafla pilav pişse deniz kadar yağ benden!"
ata5 = "Zenginin gönlü oluncaya kadar fukaranın canı çıkar!"
for ata in ata1, ata2, ata3, ata4, ata5:
    print(ata[0:-1])

print(ata[::-1])
--------------------------------------------------------------------
site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"
for a in site1,site2,site3,site4:
    print("http://"+a[0:])

print(*reversed(a))
print("\n",*enumerate(a))
-------------------------------------------------------------------
tr_harfler = "şçöğüİı"
a = 0
while a < len(tr_harfler):
    print(tr_harfler[a])
    a += 1
-------------------------------------------------------------------
met1 = metin.upper() #Buyuk harf
met2 = metin.lower() #Kucuk harf
-------------------------------------------------------------------

d1 = "python.ogg"
d2 = "tkinter.mp3"
d3 = "pygtk.ogg"
d4 = "movie.avi"
d5 = "sarki.mp3"
d6 = "filanca.ogg"
d7 = "falanca.mp3"
d8 = "dosya.avi"
d9 = "perl.ogg"
d10 = "c.avi"
d11 = "c++.mp3"
a = "c++"
for i in d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11:
    if i.startswith(a):
        print(i)
---------------------------------------------------------------------
"""
#Kayit Bolumu--------------------------------------------------------
def Giris():
    print("Otel Otomasyon Projesi\n\n\n")
    gir = int(input("""\t\t\tKayit ol---<1>
                        Oturum ac--<2>
                        Yonetici---<3>
                        >>--------->:"""))
    if gir == 1:
        Kadi = input("\nKullanici Adi   :")
        Ksif = input("Kullanici Sifre :") 
        f = open("kisi.txt","a")
        print(Kadi+"\t"+Ksif,file = f)
        f.close()
        print("\nGiris Basarili....\n")
        Islem()
    elif gir == 2:
        f = open("kisi.txt","r")
        Okunan = f.read()      
        f.close()
        Kadi = input("\nKullanici Adi   :")
        Ksif = input("Kullanici Sifre :")
        if Kadi+"\t"+Ksif in Okunan:
            print("\nGiris Basarili....\n")
            Islem()
    elif gir == 3:
        f = open("kisi.txt","r")
        Kadi = input("\n\nKullanici Adi   :")
        Ksif = input("Kullanici Sifre :")
        if Kadi+Ksif == "Serkan12345":
            print("\nGiris Basarili...\n")
            print("Kullanicilar : \n--------------")
            print(f.read())
            print("Dolu Koltuklar :")
            Yaz(1)
            Yaz(2)
            Yaz(3)
        else:
            print("Giris Basarisiz...")
            quit()   
        f.close()
#--------------------------------------------------------------------
def Yaz(n):
    if n == 1:
         print("Salon-------<1>")
         f = open("sal1.txt","r")
         dolu = f.read()
         f.close()
         dolu = dolu.replace("\n"," ")
         print(dolu)
    elif n == 2:
         print("Salon-------<2>")
         f = open("sal2.txt","r")
         dolu = f.read()
         f.close()
         dolu = dolu.replace("\n"," ")
         print(dolu)
    elif n == 3:
         print("Salon-------<3>")
         f = open("sal3.txt","r")
         dolu = f.read()
         f.close()
         dolu = dolu.replace("\n"," ")
         print(dolu)
#--------------------------------------------------------------------
def Islem():
    sal_b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    sal_i = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    sal_u = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    sec = int(input("\n<1>-5th Wave\n<2>-IP Man 3\n<3>-Deadpool\nSeciniz    :"))
    if sec == 1:
        f = open("sal1.txt","r")
        dolu_b = f.read()
        f.close()
        print("Bos Koltuklar :\n")
        dolu_b = dolu_b.replace("\n"," ")
        for s in range(1,41):
            if not str(s) in dolu_b:
                print(s)
        sec_b = int(input("Seciniz :"))
        f = open("sal1.txt","a")
        if sec_b >= 40 and sec_b <= 1:
            print("cikisssssssssssssss.")
            quit()
        else:
            print(sec_b,file = f)
        f.close()
        print("\nSecim islemi tamamlandi.")
        f = open("ucret.txt","r")
        den = int(f.read())
        f.close()
        odeme = int(input("Ogreci--1\nNormal--2  "))
        if odeme == 1:
            f = open("ucret.txt","w")
            print("Odenecek Tutar 10$")
            den += 10
            print(den,file = f)
            f.close()
        elif odeme == 2:
            f = open("ucret.txt","w")
            print("Odenecek Tutar 15$")
            den += 15
            print(den,file = f)
            f.close()
        else:
            print("Yanlis gris cikis yapildi.")
            quit()
    
    elif sec == 2:
        f = open("sal2.txt","r")
        dolu_i = f.read()
        f.close()
        print("Bos Koltuklar :\n")
        dolu_i = dolu_i.replace("\n"," ")
        for s in range(1,41):
            if not str(s) in dolu_i:
                print(s)
        sec_i = int(input("Seciniz :"))
        f = open("sal2.txt","a")
        if sec_i >= 40 and sec_i <= 1:
            print("cikisssssssssssssss.")
            quit()
        else:
            print(sec_i,file = f)
        f.close()
        print("\nSecim islemi tamamlandi.")
        f = open("ucret.txt","r")
        den = int(f.read())
        f.close()
        odeme = int(input("Ogreci--1\nNormal--2  "))
        if odeme == 1:
            f = open("ucret.txt","w")
            print("Odenecek Tutar 10$")
            den += 10
            print(den,file = f)
            f.close()
        elif odeme == 2:
            f = open("ucret.txt","w")
            print("Odenecek Tutar 15$")
            den += 15
            print(den,file = f)
            f.close()
        else:
            print("Yanlis gris cikis yapildi.")
            quit()

    elif sec == 3:
        f = open("sal3.txt","r")
        dolu_u = f.read()
        f.close()
        print("Bos Koltuklar :\n")
        dolu_u = dolu_u.replace("\n"," ")
        for s in range(1,41):
            if not str(s) in dolu_u:
                print(s)
        sec_u = int(input("Seciniz :"))
        f = open("sal1.txt","a")
        if sec_u >= 40 and sec_u <= 1:
            print("cikisssssssssssssss.")
            quit()
        else:
            print(sec_u,file = f)
        f.close()
        print("\nSecim islemi tamamlandi.")
        f = open("ucret.txt","r")
        den = int(f.read())
        f.close()
        odeme = int(input("Ogreci--1\nNormal--2  "))
        if odeme == 1:
            f = open("ucret.txt","w")
            print("Odenecek Tutar 10$")
            den += 10
            print(den,file = f)
            f.close()
        elif odeme == 2:
            f = open("ucret.txt","w")
            print("Odenecek Tutar 15$")
            den += 15
            print(den,file = f)
            f.close()
        else:
            print("Yanlis gris cikis yapildi.")
            quit()       
    else:
        print("Cikis yapildi....")
        quit()

#---------------------------------------------------------------------
#f = open("22-940x200.jpg","rb")
#o = f.read(816)
#-------------------------------------------------------------------
#import tkinter
#import tkinter.ttk as ttk
#pen = tkinter.Tk()
#btn = ttk.Button(text='merhaba', command=lambda: print('merhaba'))
#btn.pack(padx=20, pady=20)
#pen.mainloop()
"""
---------------------------------------------------------
sözlük = {"kitap" : "book","bilgisayar" : "computer","programlama": "programming"}
def ara(sözcük):
    hata = "{} kelimesi sözlükte yok!"
    print(sözlük.get(sözcük, hata.format(sözcük)))
def ekle(sözcük, anlam):
    mesaj = "{} kelimesi sözlüğe eklendi!"
    sözlük[sözcük] = anlam
    print(mesaj.format(sözcük))
def sil(sözcük):
    try:
        sözlük.pop(sözcük)
    except KeyError as err:
        print(err, "kelimesi bulunamadı!")
    else:
        print("{} kelimesi sözlükten silindi!".format(sözcük))

print('1. Sözlükte kelime ara')
print('2. Sözlüğe kelime ekle')
print('3. Sözlükten kelime sil')
no = input('Yapmak istediğiniz işlemin numarasını girin: ')
if no == '1':
    sözcük = input('Aradığınız sözcük: ')
    ara(sözcük)
elif no == '2':
    sözcük = input('Ekleyeceğiniz sözcük: ')
    anlam = input('Eklediğiniz sözcüğün anlamı: ')
    ekle(sözcük, anlam)
elif no == '3':
    sözcük = input('Sileceğiniz sözcük: ')
    sil(sözcük)
else:
    print('Yanlış işlem')

--------------------------------------------------------------

import tkinter as tk
pencere = tk.Tk()
pencere.geometry('200x70')
etiket = tk.Label(text='Merhaba Zalim Dünya')
etiket.pack()
düğme = tk.Button(text='Tamam', command=pencere.destroy)
düğme.pack()
pencere.mainloop()
-------------------------------------------------------------
import tkinter as tk
pencere = tk.Tk()
def çıkış():
    etiket['text'] = 'Elveda zalim dünya...'
    düğme['text'] = 'Bekleyin...'
    düğme['state'] = 'disabled'
    pencere.after(2000, pencere.destroy)
etiket = tk.Label(text='Merhaba Zalim Dünya')
etiket.pack()
düğme = tk.Button(text='Çık', command=çıkış)
düğme.pack()
pencere.protocol('WM_DELETE_WINDOW', çıkış)
pencere.mainloop()
-------------------------------------------------------------
"""
import tkinter
import tkinter.ttk as ttk
pencere = tkinter.Tk()
btn = ttk.Button(text='Merhaba', command=lambda: print('Merhaba'))
txt = ttk.Entry()
btn.pack(padx=20, pady=20)
txt.pack()
pencere.mainloop()






































           
