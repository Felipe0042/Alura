from sklearn.naive_bayes import MultinomialNB
from Arquivo import carregar_acessos
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings('ignore')

X, y = carregar_acessos()

X = pd.DataFrame(X)
X = X.rename(columns=X.iloc[0]).drop(X.index[0])
y = np.array(y[1:])

X_treino = X[:90]
X_teste =  X[90:]
y_treino = y[:90]
y_teste = [int(i) for i in y[90:]]

modelo = MultinomialNB()
modelo.fit(X_treino, y_treino)

resultado = [int(i) for i in modelo.predict(X_teste)]
diferenca = np.array(resultado) - np.array(y_teste)

acertos = len([d for d in diferenca if d == 0])
taxa_acerto = round(100*acertos/len(diferenca),2)
print(str(taxa_acerto) + '%')


