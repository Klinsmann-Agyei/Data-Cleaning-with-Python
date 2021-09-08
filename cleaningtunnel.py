import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob

files = glob.glob("states*.csv")

df_list = []
for filename in files:
  data = pd.read_csv(filename)
  df_list.append(data)
df = pd.concat(df_list)
print(df.columns)
print(df.dtypes)

df['Income'] = df.Income.replace('[\$,]','', regex = True)
df['Income'] = pd.to_numeric(df.Income)
df['str_split'] = df.GenderPop.str.split('_')
df['Male'] = df.str_split.str.get(0)
df['Female'] = df.str_split.str.get(1)
df['Male'] = df.Male.str[0:-1]
df['Female'] = df.Female.str[0:-1]
df.Male = pd.to_numeric(df.Male)
df.Female = pd.to_numeric(df.Female)

df = df.drop(columns = 'str_split')
print(df.head())
new_df = df.drop_duplicates()
new_df = new_df.drop(columns = "GenderPop")
print(new_df.head())
plt.scatter(new_df.Female, new_df.Income)
plt.show()
print(new_df.columns)
plt.hist(new_df.TotalPop, range(len(new_df.TotalPop)))
plt.show()
plt.hist(new_df.White, range(len(new_df.White)))
plt.show()
plt.hist(new_df.Hispanic, range(len(new_df.Hispanic)))
plt.show()
plt.hist(new_df.Black, range(len(new_df.Black)))
plt.show()
plt.hist(new_df.Native, range(len(new_df.Native)))
plt.show()
plt.hist(new_df.Asian, range(len(new_df.Asian)))
plt.show()
plt.hist(new_df.Pacific, range(len(new_df.TotalPop)))
plt.show()
plt.hist(new_df.Income, range(len(new_df.TotalPop)))
plt.show()
plt.hist(new_df.Male, range(len(new_df.TotalPop)))
plt.show()
plt.hist(new_df.Female, range(len(new_df.TotalPop)))
plt.show()
