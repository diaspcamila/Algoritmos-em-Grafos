# ATV1 - para AV1 - Teoria dos Grafos - Prof. Marcos Negreiros
## Questões teóricas - readme.md
## Questões de implementação - arquivos de código

# TODO - add imgs

### Questão 1.  
###### a) Janssen - Todas; Leuzinger - Português e pelo menos outra língua; Alain - Francês e Alemão; Medeiros - Inglês e Português. Possibilidades: 
- L falar português e apenas mais 1 língua sendo francês ou alemão / L falar português e 2 línguas sendo elas francês e alemão / L falar português e mais 2 línguas sendo elas inglês e francês OU inglês e alemão / L falar todas as línguas:
  ![1785cc04dea6adbe11ec1cb132bc1f04.png](:/d1f8f851548c4700a1250e71d6cb6bdb)
- L falar apenas português e inglês:
  ![ef45d8af9ace8ae6f3525cee867c984b.png](:/da37cba53246436d86479cf4dd08adad)
  
###### b) Leuzinger e Medeiros já conseguem se comunicar, visto que os dois falam português.
  ![ef45d8af9ace8ae6f3525cee867c984b.png](:/da37cba53246436d86479cf4dd08adad)

###### c) Ordem = n(G) = 4. Baseando-se no item a. Na possibilidade 1: Tamanho = m(G) = 5; possibilidade 2: m(G) = 4.
###### d) Excentricidade de Alain, sendo v qualquer vértice do grafo, temos E = max d(A, v) = 2.
###### e) vértice J, Janssen. Centro de um grafo G é o subgrafo induzido pelos vértices de excentricidade mínima.

### Questão 2.

### Questão 3. 
###### a) Errado ou parcialmente errado. Passa por todos os vértices de um grafo EXATAMENTE UMA VEZ. 
![1051fe8b34ace7cb5ca9e0a07d54942b.png](:/0a8a045d3dab4b2fa0b37d30ad1e096a)

###### b) Errado ou parcialmente errado. Um caminho euleriano (aberto ou fechado) é possível se o grafo for conexo e contiver zero ou dois vértices de grau ímpar, visto que com zero, pode ser formado um ciclo, e com dois, um caminho e passando em cada aresta exatamente uma vez.
Grafo com caminho euleriano: 
![b45bd87801d4a9c464aac193be64d076.png](:/66e523d168b147029b3d5a853d38160e)

###### c) Certo. 
![357bf5dbbaa605672fcb6ea16f53ee55.png](:/bb865b4f3c34450b9046e668f5164e39)

###### d) Certo. Exemplo: 
![8f1f6e21183a39e4382013d9c7dccbfe.png](:/ce78fadf637a469e88ed592e93460581)
Contrair a aresta: (1,2): 
![405e0d53981632fe3ba47e2ef54db3ba.png](:/2f8f667de2a14a8d985d57c0c60e21c2)

###### e) Errado. O termo "contração" não foi usado corretamente, um grafo linha L(G) de um grafo G e tal que:
V(L(G)) = E(G) e e1e2 ∈ E(G) ↔ e1 e e2 são incidentes em G. 
Exemplo: Antes: 
![b78f3d66e10baf2d57dc20af9e04de98.png](:/172ebb84f9964cb78eed4b689fca3879)
Depois: 
![8e5cba13c853934199d0ab41d399d707.png](:/ec6933cfa7b641c6af731c082ebd2aaf)

###### f) Correto. Duas ligações distintas em um grafo G(V, L) são ditas adjacentes se, e somente se, elas compartiham um vértice comum. 
![0708b16f495c5828af1cc9ddf08700c6.png](:/af5a144a460b4da68ab41d5dfed83843)

###### g) Correto. 
* * *
![606e92a9a4ff30bb8787286c19cf0d69.png](:/240216f55f494953a7a43b24316c2f8f)
![53135d2ce1967f7789594a4c2299bc32.png](:/4b5d7f981e094375ad5ac6e1f410e911)

### Questão 4.
