from q5 import Multigrafo, gerar_grafo_aleatorio
import itertools

def isomorfismo(grafo1, grafo2):
    if len(grafo1.vertices) != len(grafo2.vertices):
        return False

    # verificar graus e estrutura
    graus_g1 = sorted([(grafo1.grau_entrada(v.vertice_id), grafo1.grau_saida(v.vertice_id)) for v in grafo1.vertices if v.is_active])
    graus_g2 = sorted([(grafo2.grau_entrada(v.vertice_id), grafo2.grau_saida(v.vertice_id)) for v in grafo2.vertices if v.is_active])
    
    if graus_g1 != graus_g2:
        return False
    
    for perm in itertools.permutations([v.vertice_id for v in grafo2.vertices if v.is_active]):
        mapping = {v1.vertice_id: perm[i] for i, v1 in enumerate([v for v in grafo1.vertices if v.is_active])}
        if mapeamento(grafo1, grafo2, mapping):
            return True
    return False
    
def mapeamento(grafo1, grafo2, mapping):
    for origem in mapping:
        mapped_origem = mapping[origem]

        destinos_g1 = []
        atual = grafo1.buscar_vertice(origem).cabeca_arestas
        while atual:
            destinos_g1.append(atual.dest_id)
            atual = atual.next

        destinos_mapeados = sorted([mapping[dest] for dest in destinos_g1])

        destinos_g2 = []
        atual = grafo2.buscar_vertice(mapped_origem).cabeca_arestas
        while atual:
            destinos_g2.append(atual.dest_id)
            atual = atual.next
        destinos_g2 = sorted(destinos_g2)

        if destinos_mapeados != destinos_g2:
            return False
        
    return True


if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 10)
    g1.print_multigrafo()

    g2 = Multigrafo("Grafo 2")
    gerar_grafo_aleatorio(g2, 5, 10)
    g2.print_multigrafo()

    if isomorfismo(g1, g2):
        print("Os grafos são isomorfos.")
    else:
        print("Os grafos não são isomorfos.")