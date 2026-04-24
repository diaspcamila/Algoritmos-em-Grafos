from q5 import Multigrafo, gerar_grafo_aleatorio
from collections import deque

def excentricidade(self):
    excentricidades = {}

    dist = {v for v in self.vertices if v.is_active}
    total_ativos = len(dist)
    
    for vertice_obj in self.vertices:
        inicio = vertice_obj.vertice_id

        dist1 = {v.vertice_id: -1 for v in dist}
        fila = deque([inicio])
        dist1[inicio] = 0

        maior_dist = 0

        visitados = 1

        while fila:
            u = fila.popleft()

            for aresta in self.iterar_aresta(self.vertices[u].cabeca_arestas):
                v = aresta.dest_id

                if dist1[v] == -1:
                    dist1[v] = dist1[u]+1
                    maior_dist = max(maior_dist, dist1[v])
                    fila.append(v)

                    visitados += 1
                
        if visitados < total_ativos:
            excentricidades[inicio] = float('inf')
        else:
            excentricidades[inicio] = maior_dist
            
    return excentricidades
Multigrafo.excentricidade = excentricidade

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 5)

    g1.print_multigrafo()

    print(g1.excentricidade())