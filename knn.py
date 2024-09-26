import numpy as np
import pandas as pd

dataset = pd.read_csv("iris.csv")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
from sklearn.neighbors import KNeighborsClassifier

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(X_test)
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))

from sklearn.metrics import accuracy_score

print("Accuracy : ", accuracy_score(y_test, y_pred))

df = pd.DataFrame({'Real Values': y_test, 'Predicted Values': y_pred})
print(df)

new_test_point = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = classifier.predict(new_test_point)
print(f"\n Predicted class: {prediction[0]}")



OUTPUT****************








     Setosa       0.80      1.00      0.89         4
  Versicolor       1.00      0.92      0.96        13
   Virginica       1.00      1.00      1.00        13

    accuracy                           0.97        30
   macro avg       0.93      0.97      0.95        30
weighted avg       0.97      0.97      0.97        30

Accuracy :  0.9666666666666667
   Real Values Predicted Values
0   Versicolor       Versicolor
1   Versicolor       Versicolor
2   Versicolor       Versicolor
3       Setosa           Setosa
4   Versicolor       Versicolor
5   Versicolor       Versicolor
6    Virginica        Virginica
7       Setosa           Setosa
8    Virginica        Virginica
9   Versicolor       Versicolor
10  Versicolor           Setosa
11  Versicolor       Versicolor
12  Versicolor       Versicolor
13   Virginica        Virginica
14  Versicolor       Versicolor
15  Versicolor       Versicolor
16   Virginica        Virginica
17   Virginica        Virginica
18   Virginica        Virginica
19   Virginica        Virginica
20      Setosa           Setosa
21   Virginica        Virginica
22  Versicolor       Versicolor
23   Virginica        Virginica
24   Virginica        Virginica
25   Virginica        Virginica
26   Virginica        Virginica
27   Virginica        Virginica
28  Versicolor       Versicolor
29      Setosa           Setosa

