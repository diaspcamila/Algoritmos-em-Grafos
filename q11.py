from q5 import Multigrafo, gerar_grafo_aleatorio
from q7 import posorder

#cintura: A cintura de um grafo eh o comprimento do menor ciclo em G. Um
#grafo sem ciclos tem cintura infinita.

#circuferencia: 

def cintura(grafo):
    visitado = set()
    pilha_ciclo = set()
    ciclo = [float('inf')]

    # bfs p encontrar menor ciclo
    

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 10)
    
