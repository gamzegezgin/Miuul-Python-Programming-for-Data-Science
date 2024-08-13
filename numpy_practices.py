#düz python ile çözümü
import numpy as np

a = [1,2,3,4]
b = [2,3,4,5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

#numpy ile çözümü

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a*b

#numPy veri yapıları

np.array([1 ,2 ,3 ,4 ,5])
type(np.array([1, 2 ,3 ,4 ,5]))

#10 tane 0 içeren ve tipi integer olan bir array oluşturalım
np.zeros(10, dtype=int)

np.full(10, 5)

#0 ile 10 indekleri arasında random degerler içeren 10 integer içeren array oluşturalım
np.random.randint(0, 10, size=10)

#3 satır 4 sütından oluşan ortalaması 10 ve standart sapması 4 olan sayılar arrayi
np.random.normal(10, 4, (3,4))

##### NumPy Array Özellikleri (Attributes of NumPy Arrays)

#ndim: boyut sayısı
#shape: boyut bilgisi
#size: toplam eleman sayısı
#dtype: array veri tipi

#0'dan 10'a kadar sayılardan random seçilen 5 elemanlı array
a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype

##### Yeniden Şekillendirme (Reshaping)

ar = np.random.randint(1, 10, size= 6)
ar.reshape(3, 2)

##### Index İşlemleri

a = np.random.randint(10, size = 10)
a[0]
a[0:5]
a[0] = 999

b = np.random.randint(10, size = (3, 5))
b[1,4]
b[0,0] = 1

#float eklersek integer output verir

b[:, 0] #bütün satırları seç ve 0.sutunu seç
b[0:2, 0:3]

#fancy index

#0'dan 30'a kadar 3'er 3'er artacak şekilde bir array oluştur
v = np.arange(0, 30, 3)
v[1]

#uzun bir listeden tek bir komut ile belirli indexlerdeki verilere ulaşmak istediğimizde kullanırız
catch = [1, 2, 3]

v[catch]

#####Koşullu İşlemler(Conditions on NumPy)


#aşağıdaki dizide değeri 3ten küçük olan değerlere erişmek istiyoruz
v = np.array([1,2,3,4,5])

#klasik döngü ile çözüm

ab = []

for i in v:
        if i<3:
            ab.append(i)

#numpy ile çözüm

v < 3

v[v < 3]

#####Matematiksel işlemler
#metotlar

v = np.array([1,2,3,4,5])

np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.max(v)
np.var(v)

#####İki bilinmeyenli denklem çözümü

# 5*x + 2*y = 12
# x + 3*y = 10
# aşağıda bu denklemlerin ifade edilişi mevcut

a = np.array([[5, 1], [2, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)
