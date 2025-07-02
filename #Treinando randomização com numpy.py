#Treinando randomização com numpy

import numpy as np

np.random.seed(0)

Genero = np.random.choice(['Masculino', 'Feminino'],100)
Idade = np.random.randint(1,18,100)
Nota_Final = np.random.randint(0,10,100)

dados = {
    'Gênero': Genero,
    'Idade': Idade,
    'Nota Final': Nota_Final
    }

import pandas as pd

df = pd.DataFrame(dados)
df
