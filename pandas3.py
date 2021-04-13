# -*- coding: utf-8 -*-
"""Pandas3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DnOXPWJLhG-gbWQ8TfRUoU6YJgDxJ8hh
"""

import pandas as pd
alunosDictionary = {'Nome': ['Ricardo', 'Pedro', 'Roberto', 'Carlos'], 
          'Nota': [4, 7, 5.5, 9],
          'Aprovado': ['Não', 'Sim', 'Não', 'Sim']}

alunosDataFrame = pd.DataFrame(alunosDictionary)

print(alunosDataFrame)

alunosDataFrame.head()

alunosDataFrame.shape

alunosDataFrame.describe()