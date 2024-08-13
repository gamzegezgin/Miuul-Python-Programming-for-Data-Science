import pandas as pd
import seaborn as sns

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


##### Değişkeni indekse çevirmek

df["age"].head()
#df.age.head()

df.index = df["age"]

df.drop("age", axis = 1, inplace= True)
df.head()


##### İndeksi değişkene çevirmek

df.index
df["age"] = df.index
df.head()

#2.yol
df.drop("age", axis = 1, inplace= True)
df = df.reset_index().head()
df.head()

