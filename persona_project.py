import pandas as pd

# GOREV -1: Aşağıda yazanları yap.

# 1- persona.csv dosyasını okutunuz ve veri setindeki genel bilgileri gösteriniz.
pd.set_option("display.max_columns", None)
df = pd.read_csv('datasets/persona.csv')
df.head()
df.shape
df.info()

# 2- Kaç unique SOURCE vardır? Frekansları nedir?
df['SOURCE'].nunique()
df['SOURCE'].value_counts()

# 3- Kaç unique PRICE vardır?
df['PRICE'].nunique()

# 4- Hangi PRICE'dan kaç satış olmuş?
df['PRICE'].value_counts()

# 5- Hangi ülkeden kaç satış olmuş?
df.groupby("COUNTRY")["PRICE"].count()

# 6- Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# 7- SOURCE türlerine göre satış sayıları nedir?
df["SOURCE"].value_counts()

# 8- COUNTRY'lere göre PRICE ortalamaları nedir?
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# 9- SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby("SOURCE").agg({"PRICE": "mean"})

# 10- COUNRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

# GOREV -2: COUNTRY, SOURCE, SEX, AGE, AGE kırılımında ortalama kazançlar nedir?

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# GOREV -3: Çıktıyı PRICE'a göre sıralayın.

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
agg_df.head()

# GOREV -4: Indexte yer alan isimleri değişken ismine çeviriniz.

agg_df = agg_df.reset_index()
agg_df.head()

# GOREV -5: AGE değişkenini kategorik değişkene çeviriniz ve agg_df'e ekleyiniz.

agg_df["AGE"].describe()

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
my_labels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=my_labels)
agg_df.head()

# GOREV -6: Yeni level based müşterileri tanımlayınız ve veri setine değişken olarak ekleyiniz.

agg_df.columns

for row in agg_df.values:
    print(row)

[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[3].upper() + "_" + row[4].upper() + "_" + row[5].upper() for row in agg_df.values]

agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[3].upper() + "_" + row[4].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()

agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df.head()

for i in agg_df["customers_level_based"].values:
    print(i.split("-"))

agg_df["customers_level_based"].value_counts()

agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

agg_df = agg_df.reset_index()
agg_df.head()

# GOREV -7: Yeni müşterileri segmentlere ayırınız.

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

# Görev- 8: Yeni gelen müşteriyi sınıflandırıp ne kadar gelir getirecegiin tahmin et.

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

