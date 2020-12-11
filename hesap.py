import os 
os.system ("cls")

print("HOŞGELDİNİZ")

kullanıcı_adı = "kullanıcı"
parola = "12345"

while True:
    ad = input('Kullanıcı Adı:')
    parola2 = input('Parola:')
    if ((ad == kullanıcı_adı) and (parola2 == parola)):
        print("HOŞGELDİNİZ")
        break
islem = int(input("""\t(1) TOPLAMA: \n \t(2) ÇIKARMA:  \n \t(3) ÇARPMA: \n \t(4) ÜS HESAPLAMA: \n \t(5) BÖLME: \n \tYAPCAGINIZ İSLEMİ GİRİNİZ:"""))
if (islem == 1):
  sayi1 = int(input('1. sayı:'))
  sayi2 = int(input('2. sayı:'))
  print("Sonuç = {}".format(int(sayi1) + int(sayi2)))
elif (islem == 2):
  sayi3 = int(input('1. sayı:'))
  sayi4 = int(input('2. sayı:'))
  print("Sonuç = {}".format(int(sayi3) - int(sayi4)))
elif (islem == 3):
  sayi5 = int(input('1. sayı:'))
  sayi6 = int(input('2. sayı:'))
  print("Sonuç = {}".format(int(sayi5) * int(sayi6)))
elif (islem == 4):
  sayi7 =int(input('1. sayı:'))
  sayi8 =int(input('2. sayı:'))
  print("Sonuç = {}".format(int(sayi7) ** int(sayi8)))
elif (islem == 5):
  sayi9 =int(input('1. sayı:'))
  sayi10 =int(input('2. sayı:'))
  print("Sonuç = {}".format(float(sayi9) / float(sayi10)))
else:
  print("GEÇERSİZ İŞLEM")
input('Çıkmak İçin Entere Basın')
 
