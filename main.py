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

def limpar(a): #remover filmes repitidos
    top = a
    i = 0
    while i < len(top):
        j = i + 1
        while j < len(top):
            if top[j][0] == top[i][0]:
                del(top[j])
            else:
                j += 1
        i += 1
    return top

################################################ testes de run
grafoU = grafoUser(ratings) #grafo de usuarios
grafoF = grafoFilmes(filmes) #dicionario (ta como grafo mas dps percebi q nao é)

a = 1
while a != 0:
    assistido = int(input("Id do filme: "))  # adicionar busca por nome
    nota = float(input("Nota do filme: "))

    top = []
    for v in grafoU:  # recomendação
        for A in range(len(grafoU[v])):
            if assistido in grafoU[v][A] and grafoU[v][A][1] >= 3:  # filme e nota (assistiram e gostaram do filme)
                for B in range(len(grafoU[v])):
                    if grafoU[v][B][1] > 3.4 and grafoU[v][B][0] != assistido and grafoF[assistido][1] in grafoF[grafoU[v][B][0]][1] and nota > 3:
                        top.append(grafoU[v][B])
                    elif grafoU[v][B][1] > 4 and grafoU[v][B][0] != assistido and grafoF[assistido][1][4:5] in grafoF[grafoU[v][B][0]][1] and nota < 3 and grafoU[v][B][1] > 4:  # se nao gostou puxar qq filme de qq genero
                        top.append(grafoU[v][B])
                break
    top = limpar(top)  # remover filmes repitidos
    ############################################# aplicação
    print(f"Encontrado: {len(top)} filmes")
    if nota < 3:
        print(f"\nRecomendados para: {grafoF[assistido][0]}")
    else:
        print(f"{len(top)} Filmes RECOMENDADOS PARA: {grafoF[assistido][0]}\n")

    for top5 in range(20):
        if top5 >= len(top):
            break
        else:
            print(f"{grafoF[top[top5][0]]}, nota: {top[top5][1]}")
    print("\n* as notas não representam a media geral dos filmes, a ideia seria retornar a lista ordenada com base na media e gênero 👍")
    a = int(input("0 = stop, 1 = Continuar: "))
print("xau 👋")