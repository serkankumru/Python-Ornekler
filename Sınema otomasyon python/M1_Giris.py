import M2_Islem
import M3_Yaz
import time
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
        time.sleep(3)
        M2_Islem.Islem()
    elif gir == 2:
        f = open("kisi.txt","r")
        Okunan = f.read()      
        f.close()
        Kadi = input("\nKullanici Adi   :")
        Ksif = input("Kullanici Sifre :")
        if Kadi+"\t"+Ksif in Okunan:
            print("\nGiris Basarili....\n")
            time.sleep(3)
            M2_Islem.Islem()
    elif gir == 3:
        f = open("kisi.txt","r")
        Kadi = input("\n\nKullanici Adi   :")
        Ksif = input("Kullanici Sifre :")
        if Kadi+Ksif == "Serkan12345":
            print("\nGiris Basarili...\n")
            time.sleep(3)
            print("Kullanicilar : \n--------------")
            print(f.read())
            print("Dolu Koltuklar :")
            M3_Yaz.Yaz(1)
            M3_Yaz.Yaz(2)
            M3_Yaz.Yaz(3)
        else:
            print("Giris Basarisiz...")
            quit()   
        f.close()
#----------------------------------------------------------------------------

