import pandas as pd
import numpy as np
from collections import Counter

dados = pd.read_csv('busca.csv')
X = dados[['home', 'busca', 'logado']]
y = dados['comprou']
X = pd.get_dummies(X).astype(int)
print(max(Counter(y).values()))

from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = \
     train_test_split(X, y, test_size=0.1)


from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_treino, y_treino)
previsoes = model.predict(X_teste)
acertos = previsoes - y_teste
diferenca = len([d for d in acertos if d == 0])

print(('taxa de acerto: ' + str(100*diferenca/len(y_teste))) + '%')

#Algoritmo burro
previsoes_burro = np.ones(len(y_teste))
acertos_burro = previsoes_burro - y_teste
diferenca_burro = len([d for d in acertos_burro if d == 0])

print(('taxa de acerto burro: ' + str(100*diferenca_burro/len(y_teste))) + '%')







