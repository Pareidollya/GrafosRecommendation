import pandas as pd

filmes = pd.read_csv("dados/movies.csv", sep=",")
ratings = pd.read_csv("dados/ratings.csv", sep=",")

def grafoUser(ratings): #usuarios (filmes e nota) em lista de adjacencia
    print("a buildar")
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
    print("a mimir")
    return grafo

def grafoFilmes(filmes,ratings): #remover, foi so pra testar
    userId = ratings["userId"]
    userFilmes = ratings["movieId"]
    grafo = {}
    for i in filmes["movieId"]:  # montar o grafo adicionando vertices: filmes
        grafo[i] = []
    f = 0
    for j in filmes["movieId"]:  # adicionar arestas "userId" aos filmes, usuarios que assitiram au filme x (isso leva uns 7 minutoskkkkkkkkkkkkkkkkk)
        for k in userFilmes:
            if k == j:
                grafo[j].append(userId[f])
            f += 1
        f = 0
    print("\nPronto!")##
    return grafo

################################################
grafoU = grafoUser(ratings)
print("grafo completo")

usuario = int(input("Id do usuário [1 - 611]: "))
print(f"Informações o usuário: {usuario} - {len(grafoU[usuario])//2} Filmes vistos. \n['filme',nota]\n{grafoU[usuario]}") #user 611 adicionado como teste ao arquivo

######### filme trava zap
print("\naguenta um pouco q agr demora...")
grafoF = grafoFilmes(filmes,ratings)
filme = int(input("id do filme: "))
print(f"Info do filme Id {filme} - Visto por: {len(grafoF[filme])} Usuarios")

######### teste de zap, segundo run nao trava
filme = int(input("id do filme: "))
print(f"Info do filme Id {filme} - Visto por: {len(grafoF[filme])} Usuarios")
#print(len(topFilmes(filmes,userFilmes,userId)))
