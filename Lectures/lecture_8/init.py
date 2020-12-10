import pandas as pd
import numpy as np

#np_values = np.genfromtxt('data/HugoSymbol.csv', delimiter=',', dtype="S",unpack=True)
df = pd.read_csv('data/Mutation.csv', sep=',', header=None, error_bad_lines=False)

group_names = df[0].unique()

print(group_names)
print(df[25])
#df[0].value_counts().plot(kind='pie')

print(df)


#reference -> https://github.com/PacktPublishing/Pandas-Cookbook
