import pandas as pd

filmes = pd.read_csv("dados/movies.csv", sep=",")
ratings = pd.read_csv("dados/ratings.csv", sep=",")

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

def topFilmes(filmes,userFilmes,userId): #teste
    grafo = grafoFilmes(filmes,userFilmes,userId)
    numeros = []
    top10 = []
    print("terminou o grafo")
    print(len(grafo[329]),len(grafo[316]),len(grafo[307]),len(grafo[2571]))
    for x in grafo:
        numeros.append(len(grafo[x]))
        numeros.sort(reverse=True)
        top10 = numeros[0:10]
    print("d")
    for o in range(9):
        for c in grafo:
            if len(grafo[c]) == numeros[o]:
                top10.append(c)

    print("terminou o vetor")
    return top10

print(ratings["userId"])

userFilmes = ratings["movieId"]
userId = ratings["userId"]

print("passou ")

print("sun")

print("\nnovo grafo ai\n")
#print(grafoFilmes(filmes,userFilmes,userId))

print("top10")
print(topFilmes(filmes,userFilmes,userId))


#print(len(topFilmes(filmes,userFilmes,userId)))
