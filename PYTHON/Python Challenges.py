# Faktoriyel

# def factorial(num):
#     f = 1
#     for i in range(1, num+1):
#         f = f*i
#     return f
# print("0! = ", factorial(0))
# print("1! = ", factorial(1))
# print("2! = ", factorial(2))
# print("3! = ", factorial(3))
# print("4! = ", factorial(4))
# print("5! = ", factorial(5))
#############################################
# Kelimenin tersini bulmak
# isim = input("İsminizi giriniz")
# print("İsminizin tersten yazılışı: ", isim[::-1])
#############################################
# def reverse(a):
#     return a[::-1]
# print(reverse("istanbul"))
# print(reverse("erdem özen"))
#############################################
# uzunluk = len(isim)-1
# while uzunluk >= 0:
#     print(isim[uzunluk],end="")
#     uzunluk -= 1
#############################################
# Dakikayı saate çevirme
# girilenDakika = int(input("Lütfen dakikayı giriniz."))
# saat = int(girilenDakika / 60)
# dakika = girilenDakika % 60
# print("{}:{}".format(saat,dakika))
#############################################
# def convertTime(num):
#     saat = int(num / 60)
#     dakika = num % 60
#     return str(saat) +":"+ str(dakika)
#############################################
# def basHarfBuyukYap(str):
#     kelimeler = str.split(" ")
#     for i in range(0, len(kelimeler)):
#         kelimeler[i] = kelimeler[i][0].upper() + kelimeler[i][1:]
#     return " ".join(kelimeler)
# print(basHarfBuyukYap("denemek için cümle yazıyorum"))
#############################################
# def kelimeKaristirma(str1, str2):
#     for i in str2:
#         if i not in str1:
#             return False
#     return True
# print(kelimeKaristirma("istanbul","tanisbul"))
# print(kelimeKaristirma("istanbul","tanisbuk"))
#############################################
# Sıklık Bulma
# def frequency(string):
#     i = 0
#     final_string = ""
#     while i < len(string):
#         c = string[i]
#         j = i + 1
#         compressed = [1,c]
#         while j < len(string):
#             if string[j] == c:
#                 compressed[0] += 1
#             else:
#                 break
#             j += 1
#         final_string += "".join(map(str, compressed))
#         i = j
#     return final_string
# print(frequency("abcddeeefgghhhiij"))
#############################################
# Kayıp Basamak bulma
# def kayipBas(string):
#     for i in range(10):
#         c= string.replace("x",str(i))
#         d= string.index("=")
#         if eval(c[:d]) == eval(c[d+1:]):
#             return str(i)
# print(kayipBas("10 - x = 4"))
# print(kayipBas("1x * 11 = 121"))
# print(kayipBas("1x0 / 3 = 50"))
# print(kayipBas("15 * x + x = 80"))
#############################################
# Array Rotasyonu
# def rotateArray(array):
#     eski_baslangic = array[0]
#     yeni_baslangic = [str(array[eski_baslangic])]
#     count = eski_baslangic + 1
#     length = len(array)
#     while count%length != eski_baslangic:
#         yeni_baslangic.append(str(array[count%length]))
#         count += 1
#     return "".join(yeni_baslangic)
# print(rotateArray([3,4,5,6]))
# print(rotateArray([1,2,3,4,5,6,7,8,9]))
# print(rotateArray([6,2,3,4,10,6,7,8,9,11,35,48,22,34]))
#############################################
# Array Çiftleri
# def arrayCouple(array):
#     new = ""
#     for k in range(len(array)):
#         new += str(array[k]) + " "
#         if k%2 == 1:
#             new += ","
#     new = new.split(" ,")
#     depo = []
#     for i in new:
#         if i[::-1] not in new:
#             for l in i.split():
#                 depo.append(l)
#         elif i == i[::-1] and new.count(i) < 2:
#             for l in i.split():
#                 depo.append(l)
#     if depo == []:
#         return "ok"
#     return ",".join(depo)
# print(arrayCouple([3,3,4,4,4,4,5,6,6,5,6,1,1,6,4,4,4,5,5,7]))
# print(arrayCouple([3,3,4,4,4,4,3,3,5,6,6,5]))







