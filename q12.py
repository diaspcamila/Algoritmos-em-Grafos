from q5 import Multigrafo, gerar_grafo_aleatorio
from collections import deque

def excentricidade(self):
    excentricidades = {}

    for inicio in self.vertices:

        dist = {v: -1 for v in self.vertices}
        fila = deque([inicio])
        dist[inicio] = 0

        maior_dist = 0

        while fila:
            u = fila.popleft()

            for aresta in self.adj[u]:
                v = aresta.destino

                if dist[v] == -1:
                    dist[v] = dist[u]+1
                    maior_dist = max(maior_dist, dist[v])
                    fila.append(v)
                
                excentricidades[inicio] = maior_dist
            
        return excentricidades