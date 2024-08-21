import pandas as pd

########################################################################
# GOREV-1
########################################################################

df = pd.read_excel('datasets/miuul_gezinomi.xlsx')

# 1- Verisetini tanıyalım

df.info()
df.head()
df.shape

missing_values = df.isnull().sum()
print(missing_values)

pd.set_option('display.max_columns', None)

df[df['Price'].isna()]


# 2- Kaç tane unique şehir var? Frekansları nedir?

df['SaleCityName'].nunique()
df['SaleCityName'].value_counts()

# 3- Kaç unique Concept vardır?

df['ConceptName'].nunique()

# 4- Hangi Concept'ten kaçar tane satış gerçekleşmiş?

df['ConceptName'].value_counts()

# 5- Şehirlere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("SaleCityName").agg({"Price": "sum"})

# 6- Concept türlerine göre ne kadar kazanılmış?

df.groupby("ConceptName").agg({"Price": "sum"})

# 7- Şehirlere göre Price ortalamaları nedir?

df.groupby(['SaleCityName']).agg({"Price": "mean"})
# birden fazla özelliğe göre gruplanacak olsaydı by kullanılabilir ama zorunlu değil, ornegin;
# df.groupby(by=['SaleCityName', 'sth', 'sth']).agg({"Price": "mean"})

# 8- Conceptlere göre Price ortalamaları nedir?

df.groupby("ConceptName").agg({"Price": "mean"})

# 9- Şehir ve concept kırılımında price ortalaması nedir?

df.groupby(by=['SaleCityName', 'ConceptName']).agg({"Price": "mean"})

########################################################################
# GOREV-2
########################################################################

# satis_checkin_day_diff değişkenini EB_Score adlı yeni bir kategorik değişkene çevirin.

# etiketleme yapmalıyız

bins = [-1, 7, 30, 90, df["SaleCheckInDayDiff"].max()]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]

df["EB_Score"] = pd.cut(df["SaleCheckInDayDiff"], bins, labels=labels)
df.head(50).to_excel("eb_scorew.xlsx", index = False)

########################################################################
# GOREV-3
########################################################################

# Şehir, Concept, [EB_Score, Sezon, CInday] kırılımında ücret ortalamalarının frekanslarına bakınız.

df.groupby(by=['SaleCityName', 'ConceptName', 'EB_Score']).agg({"Price": "mean"})

df.groupby(by=['SaleCityName', 'ConceptName', 'Seasons']).agg({"Price": "mean"})

df.groupby(by=['SaleCityName', 'ConceptName', 'CInDay']).agg({"Price": "mean"})

########################################################################
# GOREV-4
########################################################################

# City-Concept-Season kırılımın çıktısını Price'a göre sıralayınız.

# not: Çıktıyı daha iyi görebilmemk için sort_values metodunu azalan olacak sekilde agg_df olarak kaydediniz.

agg_df = df.groupby(by=["SaleCityName", "ConceptName", "Seasons"]).agg({"Price": "mean"}).sort_values("Price", ascending = False)
agg_df.head(20)

########################################################################
# GOREV-5
########################################################################

# Indexte yer alan isimleri değişken ismine çevirin.

agg_df.reset_index(inplace=True)

agg_df.head(20)

########################################################################
# GOREV-6
########################################################################

# Yeni level based satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.

# not: sales_level_based adında bir değişken tanımlayınız ve veri setine bu değişkeni ekleyiniz.

agg_df['sales_level_based'] = agg_df[["SaleCityName", "ConceptName", "Seasons"]].agg(lambda x: '_'.join(x).upper(), axis = 1)

print(agg_df.columns)

########################################################################
# GOREV-7
########################################################################

# Price göre segmentlere ayırınız.
# segmentleri "SEGMENT" isimlendirmesi ile agg_df'e ekleyiniz.
# segmentleri betimleyiniz

agg_df["SEGMENT"] = pd.qcut(agg_df["Price"], 4, labels= ["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"Price": ["mean", "max", "sum"]})

########################################################################
# GOREV-8
########################################################################

# "ANTALYA_HERSEY DAHIL_HIGH" hangi segmenttedir ve ne kadar ücret beklenmektedir.

agg_df.sort_values(by="Price")

new_user = "ANTALYA_HERŞEY DAHIL_HIGH"
agg_df[agg_df["sales_level_based"] == new_user]