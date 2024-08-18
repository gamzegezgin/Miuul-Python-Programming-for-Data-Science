import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

#bir veriseti ile ilk karşılaşmamızda sunu yapmamız hoşluk olur

def check_df(dataframe, head = 5):
    print("######## SHAPE ########")
    print(dataframe.shape)
    print("######## TYPES #########")
    print(dataframe.dtypes)
    print("######## HEAD ########")
    print(dataframe.head(head))
    print("######## TAIL ########")
    print(dataframe.tail(head))
    print("######## NA ########")
    print(dataframe.isnull().sum())
    print("######## QUANTILES ########")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)

check_df(df)


################ Analysis of categorical variables

# bool, category ve object dtype ile bulunan kategorik degişkenlerdir
# ama bazı integerlar ile kategorilendirilen verileri tiplere bakarak bulamayız

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
print(num_but_cat)

#bazı degişkenlerin tipi categorydir fakat bunların içinden kardinalitesi yüksek olanlar vardır ki bunlar pek anlam ifade etmezler, o yüzden bunların da bulunması lazım
cat_but_cardinal = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
print(cat_but_cardinal)

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_cardinal]

df[cat_cols]

[col for col in df.columns if col not in cat_cols]


df["survived"].value_counts()
100*df["survived"].value_counts() / len(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100*dataframe[col_name].value_counts() / len(dataframe)
                        }))
    print("###########################################################")


cat_summary(df, "sex")

#döngüye sokalım
for col in cat_cols:
    cat_summary(df, col)

# cat_summary fonksiyonuna grafik de ekleyelim
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100*dataframe[col_name].value_counts() / len(dataframe)
                        }))
    print("###########################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)

################ Analysis of numerical variables
df[["age", "fare"]].describe().T


num_cols = [col for col in df.columns if df[col].dtypes in ["int", "float"]]
num_cols = [col for col in num_cols if col not in cat_cols]


def num_summary(dataframe, numerical_col):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df, "age")

for col in num_cols:
    num_summary(df, col)

def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
    print(dataframe[numerical_col].describe(quantiles).T)


    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


num_summary(df, "age", plot=True)

for col in num_cols:
    num_summary(df, col, plot=True)

################ Capturing variables and generalizing operations

