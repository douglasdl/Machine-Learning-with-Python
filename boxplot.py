# -*- coding: utf-8 -*-
"""BoxPlot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eum70isWBCFVZ-ev3WWk6nBlULyxWwXS
"""

# Load Data
from google.colab import files
uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(name=fn,length=len(uploaded[fn])))
#arquivo = "C:/ML/Vinhos/athlete_events.csv"

import pandas as pd
import io

dados = pd.read_csv(io.StringIO(uploaded['athlete_events.csv'].decode('utf-8')))

dados.head()

import matplotlib.pyplot as plt
dados.boxplot(column='Age')
plt.show()

dados.boxplot(column=['Age', 'Height', 'Weight'])
plt.show()