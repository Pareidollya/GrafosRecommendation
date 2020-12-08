# GrafosRecommendation
**Sistema de recomendação utilizando grafos em linguagem python.**

Biblioteca PandasDB para leitura dos dados em excel (necessário ter instalado).

Grafo de Usuários representado por Lista de adjacência. Onde armazena-se movieId e sua nota como valor de aresta.

Dicionario Filmes para utilizar como informações de saída.

**Para a execução do programa:

> Fazer download do projeto;

> Executar main.py;

> Inserir o filme assistido pelo seu movieId; 

> Inserir sua nota 0 - 5 (por enquanto so funcionar acima de 3);

> O retorno será uma lista de no maximo 20 filmes do mesmo gênero que foram bem avaliados por outros usuários.

**Observações:

• O codigo funciona em execução única, ou seja, mostra a recomendação com base em um único filme visto. 

• Caso o filme visto não tenha sido muito assistido ou bem avaliado pode impossibilitar a recomendação.

• movieId pode ser encontrado em movies.csv (foi adicionado novos filmes afim de testes).

**Teste usado no desenvolvimento:

*Foi adicionado 2 novos usuarios em ratings.csv com 3 filmes avaliados por cada, onde um dos filmes foi adicionado em movies.csv com movieId "1111111111" contendo gênero "Adventure". Rodando o algorítimo utilizando o filme "1111111111" como assistido, o algoritmo deve retornar os filmes que esses dois novos usuarios avaliaram com nota acima de 3 e tenham gênero "Adventure", onde, por fim deve retornar "Toy Story" e "Jumanji", filmes avaliados pelos dois que possuem gênero "Aventura".
