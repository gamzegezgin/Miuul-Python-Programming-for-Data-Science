#Görev 1
#type() kullanımı hakkında

#Görev 2
#Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry."

text1 = [word.upper() for word in text.split(" ")]
print(text1)

#text.upper().replace(","," ").replace(".", " ").split()


#Görev 3
#Adım 1: Verilen listenin eleman sayısına bakınız.
#Adım 2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
#Adım 3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
#Adım 4: Sekizinci indeksteki elemanı siliniz.
#Adım 5: Yeni bir eleman ekleyiniz.
#Adım 6: Sekizinci indekse "N" elemanını tekrar ekleyiniz

lst = ["D","A","T","A","S","C","I","E","N","C","E"]

#1
len(lst)

#2
lst[0]
lst[10]

#3
data_list = lst[0:4]
data_list

#4
del lst[8]
print(lst)

#lst.pop(8)

#5
lst.append("O")
print(lst)

#6
lst.insert(8, "N")
print(lst)

#Görev 4
#Adım 1: Key değerlerine erişiniz.
#Adım 2: Value'lara erişiniz.
#Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
#Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
#Adım 5: Antonio'yu dictionary'den siliniz.

dict = {
    'Christian': ["America", 18],
    'Daisy': ["England", 12],
    'Antonio': ["Spain", 22],
    'Dante': ["Italy", 25]
}

#1
keys = dict.keys()
print(keys)

#dict.keys() yeterli

#2
values = dict.values()
print(values)

#dict.values() yeterli

#3
dict['Daisy'][1] = 13
dict

#dict.update({"Daisy": ["England", 13]}) bu da diğer seçenek

#4
dict['Ahmet'] = ["Turkey", 24]
dict

#dict.update({"Ahmet": ["Turkey", 13]}) bu da diğer seçenek

#print(dict) yerine dict yeterli

#5
del dict['Antonio']
print(dict)

#dict.pop("Antonio")

#Görev 5
# Argüman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]

def func(l):
    even_list = []
    odd_list = []

    for index in range(len(l)):
        if l[index] % 2 == 0:
            even_list.append(l[index])
        else:
            odd_list.append(l[index])
    return even_list, odd_list


even_list, odd_list = func(l)

#Görev 6
#Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri
#bulunmaktadır. Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de
#tıp fakültesi öğrenci sırasına aittir. Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.

ogrenciler = ["Ali", "Veli", "Ayse", "Talat", "Zeynep", "Ece"]

for i, x in enumerate(ogrenciler):

    if i < 3:
        i += 1
        print("Mühendislik Fakültesi",i,".öğrenci:",x)
    else:
        i -= 2
        print("Tıp Fakültesi",i,".öğrenci:",x)

#Görev 7
#Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yeralmaktadır. Zip kullanarak ders bilgilerini bastırınız.

ders_kodu = ["CMP1005", "PSY1001", "HUK1005", "SEN2204"]
kredi = [3, 4, 2, 4]
kontenjan = [30, 75, 150, 25]

ders_bilgileri = zip(ders_kodu, kredi, kontenjan)

for kod, kredi, kontenjan in ders_bilgileri:
    print(f"Kredisi {kredi} olan {kod} kodlu dersin kontenjanı {kontenjan} kişidir.")

#Gorev 8
#Aşağıda 2 adet set verilmiştir. Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.

kume1 = set(["data", "python"])
kume2= set(["data", "function", "qcut", "lambda", "python", "miuul"])


def kume(set1, set2):

    if set1.issuperset(set2):
        print(set1.issuperset(set2))
    else:
        print(set2.difference(set1))

kume(kume1,kume2)

