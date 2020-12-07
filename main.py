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

def grafoFilmes(filmes): #remover, foi so pra testar o trava zap
    print("a buildar dnv")
    fId = filmes["movieId"]
    tFilmes = filmes["title"]
    gFilmes = filmes["genres"]
    grafo = {}
    for a in fId:  # montar o grafo adicionando vertices: filmes
        grafo[a] = []
    f = 0
    for b in fId:  # adicionar arestas "userId" aos filmes, usuarios que assitiram au filme x (isso leva uns 7 minutoskkkkkkkkkkkkkkkkk)
        grafo[b].append(tFilmes[f])
        grafo[b].append(gFilmes[f])
        f+= 1

    print("\nPronto!")##
    return grafo

################################################ testes
grafoU = grafoUser(ratings)
grafoF = grafoFilmes(filmes)

print("Ad" in grafoF[1][1])
print("Ad" in filmes["genres"][1][0:2])

print(len(grafoU[611]))
print(grafoU[611][0][0]) #usuario 611, lista 0, posição 0 😎
print(grafoU[611][1])
print(grafoU[611][2])

assistido = 240
nota = 4
top = []

print(grafoU[1][0].index(1))

if nota > 3:
    for v in grafoU:  # recomendação
        for A in range(len(grafoU[v]) - 1):
            if assistido in grafoU[v][A] and grafoU[v][A][1] >= 3:  # filme e nota (assistiram e gostaram do filme)
                for B in range(len(grafoU[v])):
                    if grafoU[v][B][1] > 3 and grafoU[v][B][0] != assistido and grafoF[grafoU[v][B][0]][1][0:2] in grafoF[assistido][1]:
                        top.append(grafoU[v][B])
                break
print(top)

#print(f"Qm viu {assistido} tb gostou: {top[0:10]}")


## teste busca de informações
usuario = int(input("Id do usuário [1 - 612]: "))
print(f"Informações o usuário: {usuario} - {len(grafoU[usuario])} Filmes vistos. \n['filme',nota]\n{grafoU[usuario]}") #user 611 adicionado como teste ao arquiv



