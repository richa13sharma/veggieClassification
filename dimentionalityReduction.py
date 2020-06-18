import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("data.csv")
print(df.head())

features = df.iloc[:, -2]
x = df.iloc[:, 0:-1]
y = df.iloc[:,-1]
x = StandardScaler().fit_transform(x)

pca = PCA(n_components=3208)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents)
finalDf = pd.concat([principalDf, df.iloc[:,-1]], axis = 1)

print(finalDf)
finalDf.to_csv("reducedData.csv")
