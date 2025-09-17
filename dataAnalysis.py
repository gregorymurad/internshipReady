### Week #4 - Data Analysis in Python

import pandas as pd
import numpy as np

df = pd.read_csv("starbucks_drinkMenu_expanded.csv")
print(df.head()) # first 5 rows
print(df.tail()) # last 5 rows
print(df.columns) # names of the columns
print(df.shape) # number of rows and number of columns

print(df.info())
print(df.describe())

df_n = df.select_dtypes(include=np.number)
print(df_n)
print(df_n.corr())

print(df["Calories"])
print(df[["Calories","Sugars (g)"]])

print(df["Calories"].mean())
print(df["Calories"].var())
print(df["Calories"].std())
print(df["Calories"].min())
print(df["Calories"].max())
print(df["Calories"].mode())

condition = df["Calories"] > 250.0
condition2 =df["Calories"] == 510.0
print(df["Calories"][condition2])
print(df[df["Calories"] == 510.0]["Beverage"])

print(df.iloc[0]) # first row
print(df.iloc[18:25]) # accessing rows 18 to 24

print(df.isna().sum()) # checking how many missing values per column
print(df[df["Caffeine (mg)"].isna()])