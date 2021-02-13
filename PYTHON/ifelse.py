""" KONTROL YAPILARI (if elif else) """


#Nested (iç içe) if örneği

# vize, final= 100, 49
# if final >= 50:
#     ort = vize * 0.4 + final * 0.6
#     if ort >= 50:
#         print("Geçtiniz.")
#     else:
#         print("Kaldınız.")
# else:
#     print("Kaldınız.")
###############################################################
#Örnek1: Cinsiyet ve boy uzunluğuna göre mülakatı geçme durumu
#Pilotluk sınavında adayların ilk aşamayı geçebilmesi için ön koşul vardır;
    #Kadınlar 1.60, Erkekler 1.70 boy sınırını geçmelidir.

# girdi = input("Lütfen cinsiyetinizi E ya da K olarak yazınız.")
# cinsiyet = girdi[0]
#
#
# if (cinsiyet == 'e' or cinsiyet == 'E'):
#     boy = int(input("Lütfen boyunuzu cm cinsinden giriniz."))
#     if boy >= 170:
#         print("Geçtiniz.")
#     else:
#         print("Kaldınız.")
# elif (cinsiyet == 'k' or cinsiyet == 'K'):
#     boy = int(input("Lütfen boyunuzu cm cinsinden giriniz."))
#     if boy >= 160:
#         print("Geçtiniz.")
#     else:
#         print("Kaldınız.")
# else:
#     print("Lütfen cinsiyetinizi e veya k olarak yazınız.")
###############################################################
#ÖRNEK2: Toptan satış programı
    #kullanıcının aldığı paket sayısına göre ödeyeceği tutarı gösteren program
    # 100paket ve üzeri paket başına 10 tl
    # 61-99 paket arası satın alımda paket başı 12
    # 30-60 paket başına 15
    # 1-29 paket 20 tl

# paket = int(input("Kaç paket aldığınızı giriniz."))
#
# if paket >= 100:
#     print("Ödeyeceğiniz tutar {} TL ' dir.".format(paket*10))
# elif  61 <= paket <= 99:
#     print("Ödeyeceğiniz tutar {} TL ' dir.".format(paket*12))
# elif  30 <= paket <= 60:
#     print("Ödeyeceğiniz tutar {} TL ' dir.".format(paket*15))
# elif  1 <= paket <= 29:
#     print("Ödeyeceğiniz tutar {} TL ' dir.".format(paket*20))
# else:
#     print("Geçerli paket tutarı giriniz.")
###############################################################
# sayi1 = int(input("Lütfen 1. sayiyi giriniz."))
# sayi2 = int(input("Lütfen 2. sayiyi giriniz."))
#
# if sayi1 < sayi2:
#     sayi1, sayi2 = sayi2, sayi1
# if sayi1 % sayi2 == 0:
#     print("{} sayısı {} sayısının tam katıdır.".format(sayi1, sayi2))
# else:
#     print("{} sayısı {} sayısının tam katı değildir.".format(sayi1, sayi2))
###############################################################
# try:
#     sayi = int(input("Lütfen bir tam sayi giriniz."))
#     sonuc = sayi % 2
#     if sonuc:
#         print("Girdiğiniz sayi tektir.")
#     else:
#         print("Girdiğiniz sayı çifttir.")
# except ValueError:
#     print("Lütfen bir tam sayi giriniz.")
###############################################################
## ASCII
# print(ord('A'))
# print(ord('♪'))
# A-Z 65-90
# a-z 97-122

# harf = input("Lütfen bir harf giriniz.")[0]
#
# if ord(harf) >= 65 and ord(harf) <= 90:
#     print("Girdiğiniz harf büyüktür.")
# elif ord(harf) >= 97 and ord(harf) <= 122:
#     print("Girdiğiniz harf küçüktür.")
# else:
#     print("Lütfen harf giriniz.")
###############################################################

# sayi1, sayi2 = float(input("Lütfen 1. sayiyi giriniz.")), float(input("Lütfen 2. sayıyı giriniz."))
#
# print(
#     """
#     Bu 2 sayıyla hangi işlemi yapmak istiyorsunuz?
#     1. Toplama
#     2. Çıkarma
#     3. Çarpma
#     4. Bölme
#     5. Mod alma
#     6. Integer Division
#     7. Üs alma
#     8. Her iki sayının karekökünü al.
#     """
# )
# secim = int(input("Lütfen işlem numarasını giriniz."))
#
# if secim == 1:
#     print(sayi1 + sayi2)
# elif secim == 2:
#     print(sayi1 - sayi2)
# elif secim == 3:
#     print(sayi1 * sayi2)
# elif secim == 4:
#     print(sayi1 / sayi2)
# elif secim == 5:
#     print(sayi1 % sayi2)
# elif secim == 6:
#     print(sayi1 // sayi2)
# elif secim == 7:
#     print(sayi1 ** sayi2)
# elif secim == 8:
#     print(sayi1 ** 0.5, sayi2 ** 0.5)
# else:
#     print("Lütfen 1-8 arası bir değer giriniz.")
###############################################################
#Örnek 6 yüksek lisans başvuru şartları
    # ALES min 60 puan, katsayısı %35
    # YDS en az 60 puan, katsayısı %25
    # AGNO en az 65(100) ve katsayısı %40
    # Başvuru puanını hesapla

# ales, yds, agno = float(input("Lütfen ALES puanınızı giriniz.")), \
#                   float(input("Lütfen YDS puanınızı giriniz.")),  \
#                   float(input("Lütfen AGNO puanınızı giriniz."))  \
#
# if ales>=60 and yds>=60 and agno>=65:
#     print("Başvurabilirsiniz ve başvuru puanınız {} .".format(ales*0.35 + yds*0.25 + agno*0.40))
# else:
#     print("Programa başvuramazsınız.")
###############################################################
#Örnek7 Kullanıcıdan 3 sayı al en büyüğü ve küçüğü yazdır.

# sayi1 ,sayi2 ,sayi3 = int(input("1. sayiyi giriniz")), \
#                       int(input("2. sayiyi giriniz")), \
#                       int(input("3. sayiyi giriniz"))
# sayilar = [sayi1, sayi2, sayi3]
#
# kucuk = min(sayilar)
# buyuk = max(sayilar)
# print("Kucuk sayı {}, buyuk sayı {}".format(kucuk, buyuk))
###############################################################
# username = "deneme"
# password = "deneme123"
# kullaniciAdi = input("Lütfen kullanici adınızı giriniz")
# sifre = input("Lütfen sifrenizi giriniz")
# if kullaniciAdi == username and sifre == password:
#     print("Basariyla giris yaptınız.")
# else:
#     print("Lütfen kullanıcı adı veya şifrenizi kontrol ediniz.")
###############################################################
#ÖRNEK Verilen değerlerle üçgen çizilir mi ?

# kenar1, kenar2, kenar3 = int(input("Lütfen 1. kenarı giriniz")), \
#                          int(input("Lütfen 3. kenarı giriniz")), \
#                          int(input("Lütfen 2. kenarı giriniz"))
# kenarlar = set([kenar1, kenar2, kenar3])
# if abs(kenar1 - kenar2) < kenar3 and kenar3 < kenar1 + kenar2:
#     if len(kenarlar) == 1:
#         print("Eşkenar üçgen")
#     elif len(kenarlar) == 2:
#         print("İkizkenar üçgen")
#     else:
#         print("Çeşitkenar üçgen")
# else:
#     print("Üçgen çizilemez.")

