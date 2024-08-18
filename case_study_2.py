##### GÖREV-1
# List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

df.columns = ["NUM" + col.upper() if df[col].dtype in [int, float] else col.upper() for col in df.columns]

##### GÖREV-2
#List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.

df.columns = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]

##### GÖREV-3

#List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.

#bu listedeki degişkenleri içermeyen yeni bir dataframe
og_list = ["abbrev", "no_previous"]

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()

#pandas egzersizleri

#Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
df = sns.load_dataset("titanic")
df.columns

#Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
gender_counts = df['sex'].value_counts()

#Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
unique_counts = df.nunique()

#Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
unique_counts_of_pclass = df['pclass'].nunique()

#Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
unique_counts_of_pclass_and_parch = df[['pclass', 'parch']].nunique()

#Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
df['embarked'].dtype
df['embarked'] = df['embarked'].astype('category')
df["embarked"].dtype
df.info()

#Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
df[df['embarked'] == "C"].head(10)

#Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
df[df['embarked'] != "S"].head(10)

df[~df['embarked'] == "S"].head(10)

#Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
df[(df['age'] < 30) & (df['sex'] == 'female')].head()

#Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
df[(df['fare'] > 500) | (df['age'] > 70)].head()

#Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
df.isnull().sum()

#Görev 12: who değişkenini dataframe’den çıkarınız.
df.drop(columns = ['who'])
df.drop("who", axis=1, inplace=True)

#Görev 13: deck değikenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
df["deck"].fillna(df["deck"].mode()[0])
#mode seri seklinde oldugu için ilk degeri almak için [0] yazıyoruz
df["deck"].isnull().sum()


#Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
df["age"] = df["age"].fillna(df["age"].median())
print(df["age"].isnull().sum())


#Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
result = df.groupby(['pclass', 'sex']).agg({"survived": ['sum', 'count', 'mean']})

#Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz. (apply ve lambda yapılarını kullanınız)

def age_30(age):
    if age < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda x : age_30(x))

#fonksiyon kullanmadan
df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

#Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
df = sns.load_dataset("tips")
df.head()
df.shape

#Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby("time").agg({"total_bill": ["sum", "min", "mean", "max"]})

#Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
df.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

#Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
df[(df["time"] == "Lunch") & (df["sex"] == "Female")].groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"],
                                                                          "tip": ["sum", "min", "max", "mean"]})

#Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
df.loc[(df["size"] < 3) & (df["total_bill"] > 10), "total_bill"].mean()

#Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
df["total_bill_tip_sum"] = df["total_bill"] + df["tip"]
df["total_bill_tip_sum"].head()

#Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape
new_df.head()