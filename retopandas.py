# -*- coding: utf-8 -*-
"""RetoPandas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tCJ-eHV4n8bPUWdzJNmhgpIk4vZrhnYH
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
from google.colab import files
pd.set_option('display.float_format', lambda x: '%.2f' % x) # truco para notación cientifica

# from google
uploaded = files.upload()

df.shape

df.head(2)

coches_mas_caros_por_ano = df.groupby('year').agg({'selling_price': 'max', 'name': 'first', "km_driven": "min",}).reset_index()

coches_mas_caros_por_ano.hist()

plt.figure(figsize=(15, 8))
plt.bar(coches_mas_caros_por_ano['year'].astype(str), coches_mas_caros_por_ano['selling_price'])
plt.xlabel('Año')
plt.ylabel('Precio del Coche Más Caro')
plt.title('Coche Más Caro por Año')

coches_mas_caros_por_ano.plot(x='year', y='selling_price', kind='bar', figsize=(15, 6))
plt.xlabel('Año')
plt.ylabel('Precio del Coche Más Caro')
plt.title('Coche Más Caro por Año')

df_agg_2015 = coches_mas_caros_por_ano[coches_mas_caros_por_ano['year']>=2015]

df_agg_2015.plot(x='year', y='selling_price', kind='bar', figsize=(15, 6))
plt.xlabel('Año')
plt.ylabel('Precio del Coche Más Caro')
plt.title('Coche Más Caro por Año')

ganga=df_agg_2015[(df_agg_2015['year'] >= 2020) & (df_agg_2015['km_driven'] <= 20000)].sort_values(by='selling_price').iloc[0]

# Muestra la información de la ganga.
print(ganga)