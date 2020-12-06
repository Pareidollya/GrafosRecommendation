import pandas as pd

filmes = pd.read_csv("dados/movies.csv", sep=",")
ratings = pd.read_csv("dados/ratings.csv", sep=",")

def grafoUser(ratings): #usuarios (filmes e nota) em lista de adjacencia
    uId = ratings["userId"]
    uFilmes = ratings["movieId"]
    uScore = ratings["rating"]
    grafo = {}
    for a in ratings["userId"]: #criar vertices
        grafo[a] = []
    x = 0

    for b in uId: #adicionar adjacencia aos vertices: filmes, valor(nota)
        grafo[b].append(f"{uFilmes[x]}") #adicionar filmes como String
        #grafo[b].append(uFilmes[x]) #adicionar filmes e notas como inteiro
        grafo[b].append(uScore[x]) #nota como inteiro ou float
        x += 1
    return grafo

def grafoFilmes(filmes,userFilmes,userId): #irei remover, foi so pra testar
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


grafoU = grafoUser(ratings)

usuario = int(input("Id do usuário [1 - 611]: "))
print(f"Informações o usuário: {usuario}\n['filme',nota]\n{grafoU[usuario]}") #user 611 adicionado como teste ao arquivo

print("top10")



#print(len(topFilmes(filmes,userFilmes,userId)))
