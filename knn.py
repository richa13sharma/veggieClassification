import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

csv = './data.csv'
dataset = pd.read_csv(csv)

# print(dataset.head())

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3781].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)


scaler = StandardScaler()
scaler.fit(X_train)


X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

print(y_pred)

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))