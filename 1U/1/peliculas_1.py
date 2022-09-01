import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv("https://raw.githubusercontent.com/rpizarrog/Analisis-Inteligente-de-datos/main/datos/movies-db.csv")

print(data.head(10))
print(data.tail(10))
print(type(data))
print(data.dtypes)
print(data.describe())

print("average_rating")
print("Valor mínimo:", data['average_rating'].min())
print("Valor máximo:", data['average_rating'].max())
print("La media aritmética:", data['average_rating'].mean())
print("Desviación Estándar:", data['average_rating'].std())
print("Núm. de observaciones:", data['average_rating'].count())


# Calculate Cost groupby foreign and genre
data.groupby(['foreign', 'genre'])['cost_millions'].sum('cost_millions').plot(kind='bar')
plt.show()

# Count the movies groupby genre
data.groupby('genre').count()['name'].plot(kind='bar')
plt.show()

print(data.groupby('foreign').agg(frequency=('foreign', 'count')))


