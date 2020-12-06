import pandas as pd

filmes = pd.read_csv("dados/movies.csv", sep=",")
ratings = pd.read_csv("dados/ratings.csv", sep=",")

print(ratings["userId"])

userFilmes = ratings["movieId"]
userId = ratings["userId"]
print(userId[10])

def grafoUser(ratings):
    grafo = {}
    for i in ratings["userId"]:
        grafo[i] = []
    return grafo

def grafoFilmes(filmes,userFilmes,userId):
    grafo = {}
    for i in filmes["movieId"]:  # montar o grafo adicionando vertices: filmes
        grafo[i] = []
    f = 0
    for j in filmes[
        "movieId"]:  # adicionar arestas "userId" aos filmes, usuarios que assitiram au filme x (isso leva uns 7 minutoskkkkkkkkkkkkkkkkk)
        for k in userFilmes:
            if k == j:
                grafo[j].append(userId[f])
            f += 1
        f = 0
    return grafo
print("passou ")

print("sun")
print(grafoUser(ratings))
print(grafoFilmes(filmes,userFilmes,userId))