from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import pandas as pd

# a arvore de decisão utilizada pela biblioteca sklearn eh uma versao otimizada do CART

dado = pd.read_csv("Dados.csv")

print(dado.head())

X = dado.iloc[:, 2:-1]
Y = dado.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=0)

dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
# dtc.predict(X_test, y_test)
plot_tree(dtc)
plt.show()
