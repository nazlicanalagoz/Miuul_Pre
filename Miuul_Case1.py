###################################################
# GÖREV 1
# Verilen değerlerin veri yapılarını inceleyiniz.
###################################################

x = 8
y = 3.2
z = 8j + 18
a = "Hello World"
b = True
c = 23 < 22
l = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Adress": "Downtown"}
t = ("Machine Learning", "Data Science")
s = {"Python", "Machine Learning", "Data Science"}

type(x)
type(y)
type(z)
type(a)
type(b)
type(c)
type(l)
type(d)
type(t)
type(s)

###################################################
# GÖREV 2
#  Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz,
#  kelime kelime ayırınız.
###################################################

text = "The goal is to turn data into information, and information into insight."

text.upper()
text.replace(",", " ").replace(".", " ")
text.split()

# Tek satırda yapalım.
text.upper().replace(",", " ").replace(".", " ").split()

###################################################
# GÖREV 3
# Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]

# Adım 1: Verilen listenin eleman sayısına bakınız.

len(lst)

# Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.

lst[0]
lst[10]

# Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.

lst1 = lst[0:4]
lst1

# Adım 4: Sekizinci indeksteki elemanı siliniz.

lst.pop(8)
lst

# Adım 5: Yeni bir eleman ekleyiniz.

lst.append("Ğ")
lst

# Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz.

lst.insert(8, "N")
lst

###################################################
# GÖREV 4
# Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict1 = {'Christian': ["America", 18], 'Daisy': ["England", 12], 'Antonio': ["Spain", 22], 'Dante': ["Italy", 25]}

# Key değerlerine erişiniz.

dict1.keys()

# Value'lara erişiniz.

dict1.values()

# Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict1["Daisy"][1] = 13
dict1


# Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict1.update({"Ahmet": ["Turkey", 24]})
dict1

# Antonio'yu dictionary'den siliniz.

dict1.pop("Antonio")
dict1

###################################################
# GÖREV 5
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri
# return eden fonksiyon yazınız.

f = [2, 13, 18, 93, 22]

def cal(sayi):

    cift_sayilar = []
    tek_sayilar = []

    for i in sayi:
        if i % 2 == 0:
            cift_sayilar.append(i)
        else:
            tek_sayilar.append(i)

    return cift_sayilar, tek_sayilar

cal(f)


###################################################
# GÖREV 6
# Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
# bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
# tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayşe", "Talat", "Zeynep", "Ece"]

for i, x in enumerate(ogrenciler):
    if i < 3:
        i += 1
        print("Mühendislik fakültesi", i, ". öğrenci:", x)
    else:
        i -= 2
        print("Tıp fakültesi", i, ". öğrenci:", x)

###################################################
# GÖREV 7
#Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer
# almaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

karsilikli = zip(ders_kodu, kredi, kontenjan)

for ders_kodu, kredi, kontenjan in karsilikli:
    print(f"Kredisi {kredi} olan {ders_kodu} numaralı dersin kontenjan sayısı {kontenjan}'dur.")

###################################################
# GÖREV 8
# Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını
# eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kumeler(set1, set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))  # ortak elemanları yaz
    else:
        print(set2.difference(set1))

kumeler(kume1, kume2)
kumeler(kume2, kume1)