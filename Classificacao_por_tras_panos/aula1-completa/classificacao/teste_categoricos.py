import pandas as pd
import numpy as np

dados = pd.read_csv('busca_nome.csv')
dados['comprou'] = dados['comprou'].replace('sim', 1).replace('nao', 0)
dados = pd.get_dummies(dados).astype(int)
