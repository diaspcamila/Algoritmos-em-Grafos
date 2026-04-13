from q5 import Multigrafo, gerar_grafo_aleatorio
from q7 import posorder
from collections import deque 

#cintura: A cintura de um grafo eh o comprimento do menor ciclo em G. Um
#grafo sem ciclos tem cintura infinita.

#circuferencia: comprimento do maior ciclo em g. Um grafo sem ciclos tem circuferencia infinita.

def cintura(grafo):
    ciclo_min = [float('inf')]

    # bfs p encontrar menor ciclo
    def bfs(inicio):
        distancia = {inicio: 0}
        fila = deque([inicio])

        while fila:
            atual = fila.popleft()

            for aresta in grafo.iterar_aresta(grafo.vertices[atual].cabeca_arestas):
                vizinho = aresta.dest_id

                if vizinho == inicio:
                    tamanho_ciclo = distancia[atual] + 1
                    if tamanho_ciclo < ciclo_min[0]:
                        ciclo_min[0] = tamanho_ciclo
                    return
                
                elif vizinho not in distancia:
                    distancia[vizinho] = distancia[atual] + 1
                    fila.append(vizinho)
    
    for v in grafo.vertices:
        if v.is_active:
            bfs(v.vertice_id)

    if ciclo_min[0] == float('inf'):
        return "Cintura infinita"
    else:
        return ciclo_min[0]

def circuferencia(grafo):
    maior_ciclo = [0]

    # backtracking p encontrar maior ciclo, codigo complexo
    def backtracking(atual, profundidade_atual, profundidades):
        profundidades[atual] = profundidade_atual

        for aresta in grafo.iterar_aresta(grafo.vertices[atual].cabeca_arestas):
            vizinho = aresta.dest_id

            #condiçao 1
            if vizinho in profundidades:
                tamanho = profundidade_atual - profundidades[vizinho] + 1
                if tamanho > maior_ciclo[0]:
                    maior_ciclo[0] = tamanho
            
            else:
                backtracking(vizinho, profundidade_atual + 1, profundidades)

        del profundidades[atual]

    for v in grafo.vertices:
        if v.is_active:
            backtracking(v.vertice_id, 0, {})
        
    if maior_ciclo[0] == 0:
        return "Circuferencia infinita"
    else:
        return maior_ciclo[0]
    

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 7)
    g1.print_multigrafo()

    print(cintura(g1))
    print(circuferencia(g1))
