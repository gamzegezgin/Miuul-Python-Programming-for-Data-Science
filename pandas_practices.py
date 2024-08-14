import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T

#en az bir tane bile eksik veri var mı?
df.isnull().values.any()

#değişkenlerin kaç eksiği var?
df.isnull().sum()

#kategorik değişkenlerde kaç sınıf var ve hangi kategoriden kaç tane var?
df["sex"].head()
df["sex"].value_counts()

##### Pandas seçim işlemleri

df.index
df[0:13]
df.drop(0,axis=0).head()

delete_indexes = [1,3,5,7]
df.drop(delete_indexes, axis = 0)
#df.drop(delete_indexes, axis = 0, inplace = True)
#inplace = True parametresi yapılan değişikliği kalıcı hale getirir


##### Değişkenler üzerinde işlemler

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

#bu secim bir pandas serisidir
df["age"].head()
type(df["age"].head())

#seçim sonucunun dataframe olarak kalmasını istiyorsak iki köşeli parantez kullanılarak işlem yapılmalı
df[["age"]].head()
type(df[["age"]].head())

df[["age", "alive", "adult_male"]]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3",axis=1).head()

#loc(label based)

#"age" ile ilgili sutunları getir
df.loc[:, df.columns.str.contains("age")].head()

#"age" ile ilgili sütunları sil, ~ işareti değildir demek, dışındakileri seçtiriyoruz
df.loc[:, ~df.columns.str.contains("age")].head()


##### Loc&Iloc

#Iloc(integer based selection
#0'dan 3'e kadar elemanları seçmek istiyoruz

df.head()
df.iloc[0:3]
df.iloc[0,0]

#loc()
df.loc[0:3]
#3'ü de gösterir

##### Koşullu seçim

#Amaç: Verisetinde yaşı 50'den büyük olanlara erişmek

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

#yaşı 50den büyük olan kişilerin class değerlerine bakmak istiyoruz
#değişkne ismi seçeceksek log ile seceriz, label based

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50)
       & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

##### Aggregation & Grouping

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

#cinsiyete göre yaş ortalamasını nasıl buluruz

df["age"].mean()

#df dataframeini cinsiyete göre grupla, ardından yaş değişkenin ortamasını al
df.groupby("sex")["age"].mean()

#alttaki kullanınm üsttekine tercih edilmeli, daha fazla aggregation uygulanması gerektiğinde işler kolaylaşır
df.groupby("sex").agg({"age": "mean"})

#örnek
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town"]).agg({"age": "mean",
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": "mean",
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({
       "age": ["mean"],
       "survived": "mean",
       "sex": "count"
})


##### Pivop Table

#pivot table group by'a benzer
#pivot tableda sırayla şunlar olur, kesişimlerde ne olacak, satırda hangi değişken, sütunda hangi degişken


df.pivot_table("survived", "sex", "embarked")
#pivot_table ön tanımlı değeri meandir.
#örneğin ön tanımı standart sapma yapmak için;
df.pivot_table("survived", "sex", "embarked", aggfunc="std")

#yaşa göre analiz yapmak için yaş değişkenini kategorik degişkene çevirebiliriz

#cut ve qcut fonksiyonları sayısal değişkenleri kategorik değişkenlere çevirmek için en kullanışlı fonksiyonlardır
#neye gore bölecegimizi biliyorsak cut, özel bir kategorilendirme yaomadan çeyreklik olarak böleceksek qcut kullanılır


df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])
df.head()

df.pivot_table("survived", "sex", ["new_age", "class"])

#tüm çıktıyı yanyana alabilmek için bu komutu çalıştırırız
pd.set_option('display.width', 500)


##### Apply & Lambda

#lambda kullan at fonksiyondur
#apply fonksiyonu elimizdeki satır suturlara fonksiyon uygulamaya yarar

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5
df.head()

#new_age string oldugu için matematiksel işlem uygulanamaz hata alırız o yüzden çıkardık
df.loc[:, df.columns.str.contains("age")].drop("new_age", axis = 1).apply(lambda x: x/10).head()


#####join işlemleri

m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

#iki dataframei altalta birleştirmek istersek concat metodu
#default olarak alt alta ekler eğer column eklemek istersek axis=1 olarak ayarlarız
pd.concat([df1, df2], ignore_index=True)

#merge ile birleştirme

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
#pd.merge(df1, df2, on="employees")

df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)



























































