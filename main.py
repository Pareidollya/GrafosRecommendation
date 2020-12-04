import pandas as pd
import numpy as np

FILMES = pd.read_csv("dados/movies.csv", usecols=["movieId","title"],sep=",")
ratings = pd.read_csv("dados/ratings.csv", usecols=['userId','movieId','rating'],sep=",")
#tags = pd.read_csv("dados/tags.csv", usecols=['userId','movieId'])

filmeId = FILMES["movieId"].values#vertice

UserId = ratings["userId"].values
UserFilmes = ratings["movieId"].values

grafo = {}
for i in filmeId: #
    grafo[i] = []

print("passou ")

for j in filmeId:

    for k in UserFilmes:
        if k == j:
            grafo[j].append(k)
    j += 1

print("sun")








