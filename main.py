import pandas as pd

filmes = pd.read_csv("dados/movies.csv", sep=",")
ratings = pd.read_csv("dados/ratings.csv", sep=",")

def grafoUser(ratings): #linked list
    print("a buildar")
    uId = ratings["userId"]
    uFilmes = ratings["movieId"]
    uScore = ratings["rating"]
    grafo = {}

    for a in ratings["userId"]: #criar vertices
        grafo[a] = []
    x = 0
    for b in uId: #adicionar adjacencia aos vertices: filmes, valor(nota)
        l = []
        l.append(uFilmes[x])
        l.append(uScore[x])
        grafo[b].append(l)
        x += 1
    print("a mimir")
    return grafo

def grafoFilmes(filmes,ratings): #remover, foi so pra testar o trava zap
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

################################################ testes
grafoU = grafoUser(ratings)
print(len(grafoU[1]))
print(len(grafoU[611]))
print(grafoU[611][0][0]) #usuario 611, lista 0, posição 0 😎
print(grafoU[611][1])
print(grafoU[611][2])

assistido =1111111111
nota = 4
top = []

for v in grafoU: #recomendação
    if grafoU[v][0][0] == assistido and grafoU[v][0][1] >= 3: #filme e nota (assistiram e gostaram do filme)
        print("ae achou o filme heim ")
        aux = 0
        for f in grafoU[v]:
            if grafoU[v][aux][1] > 3 and grafoU[v][aux] != assistido:
                top.append(grafoU[v][aux])
            aux += 1

print(f"Qm viu tb gostou: {top}")


## teste busca de informações
usuario = int(input("Id do usuário [1 - 612]: "))
print(f"Informações o usuário: {usuario} - {len(grafoU[usuario])} Filmes vistos. \n['filme',nota]\n{grafoU[usuario]}") #user 611 adicionado como teste ao arquiv



