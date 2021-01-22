#LOOPS (Döngüler)

# gunler = ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma', 'Cumartesi', 'Pazar']
#
# i = 0
# while i < 7:
#     print(gunler[i], end=" ")
#     j = i + 1
#     while j <= 31:
#         print(j, end=" ")
#         j += 7
#     print()
#     i += 1
#########################################################
# sayi = int(input("Lütfen bir sayı giriniz."))
# sayiDegerleri = []
# while sayi > 0:
#     sayiDegeri = sayi % 10
#     sayi //= 10
#     sayiDegerleri.append(sayiDegeri)
# print(sayiDegerleri)
# print("Sayı değerleri toplamı:", sum(sayiDegerleri))
#########################################################
#Faktöriyel
# try:
#     n = int(input("Faktöriyelini öğrenmek istediğiniz sayıyı giriniz."))
#     if n >= 0:
#         i = 1
#         sonuc = 1
#         while i <= n:
#             sonuc *= i
#             i += 1
#         print(sonuc)
#     else:
#         print("Lütfen doğal sayı giriniz.")
# except ValueError:
#     print("Lütfen tam sayı giriniz.")
#########################################################
# Örnek 7 - Restoran Menü Programı
# """
# Hoşgeldiniz, ne arzu edersiniz?
#     1. Adana/Urfa   20TL
#     2. Beyti        25TL
#     3. İskender     30TL
#     4. Çorba        10TL
#     5. Tatlı        15TL
#     6. İçecek       5TL
#     7. ÇIKIŞ
# """
#
# print("""
# Hoşgeldiniz, ne arzu edersiniz?
#     1. Adana/Urfa   20TL
#     2. Beyti        25TL
#     3. İskender     30TL
#     4. Çorba        10TL
#     5. Tatlı        15TL
#     6. İçecek       5TL
#     7. ÇIKIŞ
# """)
# toplamTutar = 0
# while True:
#     siparis = int(input("Lütfen sipariş vermek istediğiniz ürünün numarasını giriniz."))
#     if siparis > 0 and siparis < 7:
#         adet = int(input("Bu üründen kaç adet sipariş vermek istersiniz?"))
#     if siparis == 1:
#         toplamTutar += 20 * adet
#     elif siparis == 2:
#         toplamTutar += 25 * adet
#     elif siparis == 3:
#         toplamTutar += 30 * adet
#     elif siparis == 4:
#         toplamTutar += 10 * adet
#     elif siparis == 5:
#         toplamTutar += 15 * adet
#     elif siparis == 6:
#         toplamTutar += 5 * adet
#     elif siparis == 7:
#         print("Siparişiniz için teşekkür ederiz.")
#         break
# print("Toplam tutar: ", toplamTutar, "TL")
#########################################################
# tupleListesi = [(21, 34), (41, 54), (0, -11), (-5, -7)]
# for tup in tupleListesi:
#     print(tup, end=" ")
# print()
# for tup1, tup2 in tupleListesi:
#     print(tup1, tup2, end=" ")
#########################################################
# sayi1 = int(input("Lütfen 1. sayiyi giriniz"))
# sayi2 = int(input("Lütfen 2. sayiyi giriniz"))
#
# sayilar = list(range(sayi1, sayi2+1))
# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
# print(toplam)
#########################################################
# sayilar = [2, 3, 4, 5, 61, 2, 3, 4, 5, 6, -5, -7, -9, 0, 1, 2, 3, 4, 5]
# ciftListe = []
# tekListe = list()
#
# for sayi in sayilar:
#     if sayi % 2 == 0:
#         ciftListe.append(sayi)
#     else:
#         tekListe.append(sayi)
#
# print("Tek sayılar: {} ve {} tane tek sayı bulunmaktadır.".format(tekListe, len(tekListe)))
# print("Çift sayılar: {} ve {} tane çift sayı bulunmaktadır.".format(ciftListe, len(ciftListe)))
#########################################################
# for i in range(1, 11):
#     for j in range(1, 11):
#         print("{}x{}={}".format(j,i,j*i), end="     ")
#     print()
#########################################################
# from math import sqrt
# for sayi in range(1, 1001):
#     if int(sqrt(sayi)) ** 2 == sayi:
#         print("Karekök", sayi, "=", sqrt(sayi),"  ", sayi, "karekökü tam sayı olan bir sayıdır.")
#########################################################
# ogr1 = {'isim': 'Erdem', 'vizeNotlari': [100, 85], 'finalNotu': 90}
# ogr2 = {'isim': 'Oğuzhan', 'vizeNotlari': [95, 85], 'finalNotu': 80}
# ogr3 = {'isim': 'Beyaz', 'vizeNotlari': [70, 78], 'finalNotu': 85}
# ogr4 = {'isim': 'Ömer', 'vizeNotlari': [95, 85], 'finalNotu': 78}
# ogr5 = {'isim': 'Burak', 'vizeNotlari': [80, 84], 'finalNotu': 61}
# ogrenciler = [ogr1, ogr2, ogr3, ogr4, ogr5]
# ogrencilerinDonemSonuNotToplami = 0
# for ogrenci in ogrenciler:
#     ogrDonemSonuNot = ogrenci['vizeNotlari'][0] * 0.25 + ogrenci['vizeNotlari'][1] * 0.35 + ogrenci['finalNotu']* 0.40
#     #print(ogrDonemSonuNot)
#     ogrencilerinDonemSonuNotToplami += ogrDonemSonuNot
# ogrencilerinDonemSonuNotOrtalamasi = ogrencilerinDonemSonuNotToplami / len(ogrenciler)
# #print(ogrencilerinDonemSonuNotOrtalamasi)
# for ogrenci in ogrenciler:
#     ogrDonemSonuNot = ogrenci['vizeNotlari'][0] * 0.25 + ogrenci['vizeNotlari'][1] * 0.35 + ogrenci['finalNotu']* 0.40
#     if ogrDonemSonuNot >= ogrencilerinDonemSonuNotOrtalamasi:
#         print("Öğrenci Adı: {} ortalaması: {} Bu öğrenci dersi geçti.".format(ogrenci['isim'], ogrDonemSonuNot))
#     else:
#         print("Öğrenci Adı: {} ortalaması: {} Bu öğrenci dersten kaldı.".format(ogrenci['isim'], ogrDonemSonuNot))
# print("Geçme Notu: ", round(ogrencilerinDonemSonuNotOrtalamasi, 2))
#########################################################
# while True:
#     n = float(input("Lütfen karesini öğrenmek istediğiniz sayıyı giriniz.Çıkmak için 0'ı tuşlayınız."))
#     if n == 0:
#         break
#     print(n, "karesi", n ** 2)
#########################################################
# sayi = int(input("Lütfen 0-10 arası bir tam sayı giriniz."))
# for i in range(10):
#     if i != sayi:
#         print(i)
#     else:
#         break
#########################################################
#Enumerator

# enum = enumerate("Erdem ÖZEN")
# print(enum)
# print(list(enum))
#########################################################
# for index, harf in enumerate('Erdem ÖZEN'):
#     if harf == 'M' or harf == 'm':
#         print("{} harfi {}. indextedir.".format(harf, index))
#         break
#########################################################
# secret_pass = "A1"
# count_pass = 3
# try0 = 0
#
# for i in range(count_pass):
#      sifre = input("Lütfen şifrenizi giriniz.")
#      if sifre == secret_pass:
#         print("Başarıyla giriş yaptınız")
#         break
#      else:
#          print("Yanlış şifre girdiniz.")
#          try0 += 1
#          if try0 == 3:
#              print("3 defa hatalı giriş yaptığınız için oturumunuz sonlandı.")
#########################################################
#ÖRNEK5 Defter satan bir e-ticaret sitesinde defter satın almak isteyen bir müşteriye
#   #kaç adet defter almak istediğini soran ve kullanıcının istediği defter sayısını
#   #stokla kontrol ederek kullanıcıya tepki veren programı yazınız.
#   # 5 defter alırsa 5 defa " 1 adet defter sepete eklendi." yazsın.
#   # (Stok miktarı başlangıçta 10 olsun)

# stok = 10
# adet = int(input("Lütfen kaç adet defter almak istediğinizi giriniz."))
#
# if adet <= stok:
#     for i in range(adet):
#         print("1 adet defter sepete eklendi.")
#     stok -= adet
# else:
#     print("Stokta {} adet defter kaldığından dolayı işleminizi gerçekleştiremiyoruz.".format(stok))
#########################################################

# ATM ÖRNEĞİ
# başlangıç bakiyesi 500tl
# 3 defa yanlış şifre girilince kart bloke olacaktır.
# para çekme, para yatırma, bakiye sorgulama ve kart iade işlemleri

# bakiye, secret_pass, count_pass, login = 500, 1234, 3, False
# while True:
#      if login == False:
#         sifre = int(input("Lütfen şifrenizi giriniz."))
#      if sifre == secret_pass:
#          login = True
#          print("""
#          1. Para çekme
#          2. Para yatırma
#          3. Bakiye sorgulama
#          4. Kart iade
#          """)
#          islemNo = int(input("Lütfen işlem numarasını tuşlayınız."))
#          if islemNo == 1:
#              paraCekme = int(input("Lütfen çekmek istediğiniz tutarı giriniz."))
#              if paraCekme > bakiye:
#                  print("Yeterli bakiyeniz bulunmamaktadır.")
#                  continue
#              else:
#                  if paraCekme > 0:
#                     bakiye -= paraCekme
#                  print("Yeni bakiyeniz: {} TL".format(bakiye))
#          elif islemNo == 2:
#              paraYatirma = int(input("Lütfen yatırmak istediğiniz miktarı giriniz."))
#              if paraYatirma > 0:
#                 bakiye += paraYatirma
#              print("Yeni bakiyeniz: {} TL".format(bakiye))
#          elif islemNo == 3:
#              print("Mevcut bakiyeniz: {} TL".format(bakiye))
#              continue
#          elif islemNo == 4:
#              print("Kartınız iade ediliyor.")
#              break
#          else:
#              print("Lütfen geçerli işlem numarasını tuşlayınız.")
#      else:
#          print("Yanlış şifre girdiniz.")
#          count_pass -= 1
#          if count_pass == 0:
#              print("3 defa hatalı giriş yaptığınız için oturumunuz sonlandı.")
#              break
#########################################################

## For-else

# sayilar = [3, 5, 7]
# for sayi in sayilar:
#     if sayi % 2 == 0:
#         print("{} çift sayıdır".format(sayi))
#         break
# else:
#     print("Çift sayı bulunamamaktadır")
#########################################################

# from math import sqrt
# sayi = int(input("Lütfen bir sayı giriniz."))
# for i in range(2, int(sqrt(sayi) + 1)):
#     if sayi % i == 0:
#         print("{} asal sayı değildir.".format(sayi))
#         break
# else:
#     print("{} Asal sayıdır.".format(sayi))
#########################################################
# from math import sqrt
#
# for i in range(2, 1001):
#     for j in range(2, int(sqrt(i) + 1)):
#         if i % j == 0:
#             break
#     else:
#         print("{} asal sayıdır.".format(i))
#########################################################
# try:
#     n = int(input("Faktöriyelini öğrenmek istediğini sayıyı giriniz."))
#     if n<0:
#         print("Lütfen bir doğal sayı giriniz.")
#     else:
#         sonuc = 1
#         for i in range(1, n+1):
#             sonuc *= i
#
#         print("{}! = {}".format(n, sonuc))
# except ValueError:
#     print("Lütfen tam sayı giriniz")
#########################################################
# terimSayisi = int(input("Kaç tane terim görüntülemek istiyorsunuz."))
# n1, n2 = 0, 1
# count = 0
# if terimSayisi <= 0:
#     print("Lütfen pozitif bir tam sayı giriniz.")
# elif terimSayisi == 1:
#     print(n1)
# else:
#     while count < terimSayisi:
#         print(n1, end=" ")
#         n3 = n1 + n2
#         n1 = n2
#         n2 = n3
#         count += 1
#########################################################
# Kullanıcının girdiği 2 tam sayının EBOB'unu bulan program
# x = int(input("Lütfen 1. sayıyı giriniz"))
# y = int(input("Lütfen 2. sayıyı giriniz"))
# sayi1 = x
# sayi2 = y
#
# while y:
#     x, y = y, x%y
# print("EBOB ({}, {}) = {}".format(sayi1, sayi2, x))
#########################################################























