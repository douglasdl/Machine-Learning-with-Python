# -*- coding: utf-8 -*-
"""Listas.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Nn35XKF2cRVqH6ZHegsZ68gSQs_jHVXx
"""

# Create List
lista1 = [1, 2, 3]

# Check Type
type(lista1)

# Create List of Lists
lista2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Check Type
type(lista2)

# Get List Element by Index
lista2[0]

# Get List Element by Index
lista2[0][1]

select = lista2[1][1]
print(select)
type(select)

# Import Library
import random
cidades = ['Hirakata', 'Osaka', 'Kyoto', 'Tokyo']
escolhida = random.choice(cidades)
print('The choosen city is:', escolhida)

a = [1, 2, 3]
print(a)

# Add an element to the end of the list
a.append(15)
print(a)

b = [7, 8, 9]
print(b)

# Add elements from one list to the end of another list
for item in b:
  a.append(item)
print(a)