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
