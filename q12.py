from q5 import Multigrafo, gerar_grafo_aleatorio
from collections import deque

def excentricidade(self):
    excentricidades = {}

    for vertice_obj in self.vertices:
        inicio = vertice_obj.vertice_id

        dist = {v.vertice_id: -1 for v in self.vertices}
        fila = deque([inicio])
        dist[inicio] = 0

        maior_dist = 0

        while fila:
            u = fila.popleft()

            for aresta in self.iterar_aresta(self.vertices[u].cabeca_arestas):
                v = aresta.dest_id

                if dist[v] == -1:
                    dist[v] = dist[u]+1
                    maior_dist = max(maior_dist, dist[v])
                    fila.append(v)
                
        excentricidades[inicio] = maior_dist
            
    return excentricidades
Multigrafo.excentricidade = excentricidade

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 5)

    g1.print_multigrafo()

    print(g1.excentricidade())