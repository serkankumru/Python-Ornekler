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
