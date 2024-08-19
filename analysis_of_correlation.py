import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("datasets/data.csv")
df = df.iloc[:, 1:-1]
df.head()

#yüksek korelasyonlu degerleri yakalama

num_cols = [col for col in df.columns if df[col].dtype in [int,float]]
corr = df[num_cols].corr()

sns.set(rc = {'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

# yüksek korelasyonlu değişkenlerin silinmesi

cor_matrix = df.corr().abs()

#korelasyon tablosunda tekrar eden ve veri kalabalığı yapan kısımları çıkartıyoruz, mesela a ve b nin korelasyonuna bakıldı, b ve a nın korelasyonuna bakılmaya gerek yok

upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(np.bool_))

#bazen cok yüksek korelasyona sahip degerlerden birini silmemiz gerekir cunkü neredeyse aynı sonucu vereceklerdir

drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.9)]

cor_matrix[drop_list]

df.drop(drop_list, axis =1)

