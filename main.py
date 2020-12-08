import pandas as pd
#leitura de dados
filmes = pd.read_csv("dados/movies.csv", sep=",")
ratings = pd.read_csv("dados/ratings.csv", sep=",")

def grafoUser(ratings): #lista de adjacencia
    uId = ratings["userId"]
    uFilmes = ratings["movieId"]
    uScore = ratings["rating"]
    grafo = {}
    for a in ratings["userId"]: #criar vertices referentes a cada usuario
        grafo[a] = []
    x = 0
    for b in uId: #adicionar adjacencia aos vertices: filmes, valor(nota)
        l = []
        l.append(uFilmes[x])
        l.append(uScore[x])
        grafo[b].append(l)
        x += 1
    return grafo

def grafoFilmes(filmes):
    fId = filmes["movieId"]
    tFilmes = filmes["title"]
    gFilmes = filmes["genres"]
    grafo = {}
    for a in fId:
        grafo[a] = []
    f = 0
    for b in fId:  #adicionar "titulo" e "genero" referente a cada "movieId"
        grafo[b].append(tFilmes[f])
        grafo[b].append(gFilmes[f])
        f+= 1
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

print("SISTEMA DE RECOMENDAÇÃO\n")
grafoU = grafoUser(ratings) #grafo de usuarios
grafoF = grafoFilmes(filmes) #dados dos filmes

a = 1
while a != 0:
    assistido = int(input("Id do filme: "))  # adicionar busca por nome
    nota = float(input("Nota do filme: "))
    top = []
    for v in grafoU:  # recomendação
        for A in range(len(grafoU[v])):
            if assistido in grafoU[v][A] and grafoU[v][A][1] >= 3:  # filme e nota (assistiram e gostaram do filme)
                for B in range(len(grafoU[v])):
                    if grafoU[v][B][1] > 3.4 and grafoU[v][B][0] != assistido and grafoF[assistido][1] in grafoF[grafoU[v][B][0]][1] and nota > 3: #filmes parecidos
                        top.append(grafoU[v][B])
                    elif grafoU[v][B][1] > 4 and grafoU[v][B][0] != assistido and grafoF[assistido][1][4:5] in grafoF[grafoU[v][B][0]][1] and nota < 3 and grafoU[v][B][1] > 4: #filmes quase parecidos
                        top.append(grafoU[v][B]) #para ajustar a acuracia de notas alterar: grafoU[v][B][1] > 4, para gênero: grafoF[assistido][1][4:5]
                break
    top = limpar(top)

    #aplicação
    print(f"Encontrado: {len(top)} filmes")
    if nota < 3:
        print(f"\nRecomendação para: {grafoF[assistido][0]}.")
    else:
        print(f"{len(top)} Filmes RECOMENDADOS PARA: {grafoF[assistido][0]}\n")

    if len(top) > 0:
        for top20 in range(20):
            if top20 >= len(top):
                break
            else:
                print(f"{grafoF[top[top20][0]]}, nota: {top[top20][1]}")
    else:
        print(f"Erro: Não foi possível encontrar dados de outros usuarios com base nas informações inseridas!")
    print("\n* as notas não representam a media geral dos filmes, a ideia seria retornar a lista ordenada com base na media e gênero 👍")
    a = int(input("0 = stop, 1 = Continuar: "))
print("tchau 👋")