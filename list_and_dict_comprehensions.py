#####UYGULAMA-1

#########################
# Bir Veri Setindeki Değişkenlerin İsimlerini Değiştirmek
#########################

# before:
# ['total', 'speeding', 'alcohol', 'not_distracted', 'no_previous', 'ins_premium', 'ins_losses', 'abbrev']

# after:
# ['TOTAL', 'SPEEDING', 'ALCOHOL', 'NOT_DISTRACTED', 'NO_PREVIOUS', 'INS_PREMIUM', 'INS_LOSSES', 'ABBREV']

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

for col in df.columns:
    print(col.upper())

#bu değişimi kalıcı bir şekilde dataframe yansıtmak istiyoruz

#liste formatına getirelim

A = []
for col in df.columns:
    A.append(col.upper())

df.columns = A

#buraya kadar yaptıgımız list comprehension kullanmadan bunu çözmekti
#bundan sonraki aşamada aynı sonuca list comprehension ile nasıl ulaşacagımıza bakacagız

df = sns.load_dataset("car_crashes")

df.columns = [col.upper() for col in df.columns]

#####UYGULAMA-2

#########################
# İsmi̇nde "INS" olan değişkenleri̇n başına FLAG, diğerleri̇ne NO_FLAG eklemek i̇sti̇yoruz.
#########################

# before:
# ['TOTAL',
# 'SPEEDING',
# 'ALCOHOL',
# 'NOT_DISTRACTED',
# 'NO_PREVIOUS',
# 'INS_PREMIUM',
# 'INS_LOSSES',
# 'ABBREV']

# after:
# ['NO_FLAG_TOTAL',
# 'NO_FLAG_SPEEDING',
# 'NO_FLAG_ALCOHOL',
# 'NO_FLAG_NOT_DISTRACTED',
# 'NO_FLAG_NO_PREVIOUS',
# 'FLAG_INS_PREMIUM',
# 'FLAG_INS_LOSSES',
# 'NO_FLAG_ABBREV']



["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]

#eğer aşağıdaki işlemi yaparsak yeni kolon adlarını dataframe kolon isimleri haline getiririz

#df.columns = ["FLAG_" + col if "INS" in col else "NO_FLAG_" + col for col in df.columns]


#####UYGULAMA-2

#########################
# Amaç key'i string, value'su aşağıdaki gibi bir liste olan sözlük oluşturmak.
# Bu işlemi sadece sayısal değişkenler için yapmak istiyoruz.
#########################

# Output:
# {'total': ['mean', 'min', 'max', 'var'],
# 'speeding': ['mean', 'min', 'max', 'var'],
# 'alcohol': ['mean', 'min', 'max', 'var'],
# 'not_distracted': ['mean', 'min', 'max', 'var'],
# 'no_previous': ['mean', 'min', 'max', 'var'],
# 'ins_premium': ['mean', 'min', 'max', 'var'],
# 'ins_losses': ['mean', 'min', 'max', 'var']}

#bu çalışmada dictionary comprehension kullanılacak

import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns

#sadece sayısal verileri seç

num_cols = [col for col in df.columns if df[col].dtype != "O"]
#söz konusu dataframe içindeki verisetinin içersinde tipi object olmayanları seç

soz = {}
agg_list = ["mean", "min", "max", "sum"]

#key değeri değişkenler, value değeri agg_list olmalı

for col in num_cols:
    soz[col] = agg_list

#dict comprehension ile kısa yol çözüm

{col: agg_list for col in num_cols}

#örnek kullanım senaryosu

new_dict = {col: agg_list for col in num_cols}

df[num_cols].head()

df[num_cols].agg(new_dict)

#tek hamle ile agg fonksiyonunu hepsine uyguladık