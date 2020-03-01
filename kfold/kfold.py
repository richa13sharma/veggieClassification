import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.preprocessing import StandardScaler


csv = '../data.csv'
dataset = pd.read_csv(csv)

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values



# knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
# knn.fit(X_train, y_train)
# y_pred = knn.predict(X_test)
# print(metrics.accuracy_score(y_test, y_pred))

# from sklearn.model_selection import KFold
# kf = KFold(n_splits=5, shuffle=False)

from sklearn.model_selection import cross_val_score

knn = KNeighborsClassifier(n_neighbors=5)
scores = cross_val_score(knn, X, y, cv=10, scoring='accuracy')
print(scores)
print(scores.mean())


