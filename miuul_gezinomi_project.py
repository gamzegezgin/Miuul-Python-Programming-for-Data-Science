import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


data = pd.read_excel('datasets/miuul_gezinomi.xlsx')

# 1- Verisetini tanıyalım

data.info()
data.head()
data.shape

missing_values = data.isnull().sum()
print(missing_values)

pd.set_option('display.max_columns', None)

data[data['Price'].isna()]


# 2- Kaç tane unique şehir var? Frekansları nedir?

