from q5 import Multigrafo, gerar_grafo_aleatorio
import math

def arestas_como_conjunto(grafo):
    edges = set()
    for v in grafo.vertices:
        if v.is_active:
            for aresta in grafo.iterar_aresta(v.cabeca_arestas):
                if grafo.vertices[aresta.dest_id].is_active:
                    edges.add((v.vertice_id, aresta.dest_id))
    return edges


def vetor_graus(grafo):
    ids_ativos = [v.vertice_id for v in grafo.vertices if v.is_active]
    if not ids_ativos:
        return []
    tamanho = max(ids_ativos) + 1
    vetor = [0] * tamanho
    for v in grafo.vertices:
        if v.is_active:
            vetor[v.vertice_id] = grafo.soma_graus(v.vertice_id)
    return vetor

def jaccard(grafo1, grafo2):
    e1 = arestas_como_conjunto(grafo1)
    e2 = arestas_como_conjunto(grafo2)
    intersecao = len(e1 & e2)
    uniao = len(e1 | e2)
    if uniao == 0:
        return 1.0  
    return intersecao / uniao

def cosseno(grafo1, grafo2):
    v1 = vetor_graus(grafo1)
    v2 = vetor_graus(grafo2)

    tamanho = max(len(v1), len(v2))
    v1 += [0] * (tamanho - len(v1))
    v2 += [0] * (tamanho - len(v2))

    produto_interno = sum(a * b for a, b in zip(v1, v2))
    norma1 = math.sqrt(sum(a ** 2 for a in v1))
    norma2 = math.sqrt(sum(b ** 2 for b in v2))

    if norma1 == 0 or norma2 == 0:
        return 0.0
    return produto_interno / (norma1 * norma2)


def sobreposicao(grafo1, grafo2):
    e1 = arestas_como_conjunto(grafo1)
    e2 = arestas_como_conjunto(grafo2)
    intersecao = len(e1 & e2)
    minimo = min(len(e1), len(e2))
    if minimo == 0:
        return 1.0 if intersecao == 0 else 0.0
    return intersecao / minimo


def similaridade(grafo1, grafo2):
    j = jaccard(grafo1, grafo2)
    c = cosseno(grafo1, grafo2)
    s = sobreposicao(grafo1, grafo2)

    print(f"\nSimilaridade entre '{grafo1.name}' e '{grafo2.name}':")
    print(f"  Jaccard             : {j:.4f}  (0=nenhuma, 1=idênticos)")
    print(f"  Cosseno             : {c:.4f}  (0=ortogonais, 1=paralelos)")
    print(f"  Coef. Sobreposição  : {s:.4f}  (0=disjuntos, 1=um contido no outro)")

    return {"jaccard": j, "cosseno": c, "sobreposicao": s}


if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    g1.add_vertice(1, "A"); g1.add_vertice(2, "B"); g1.add_vertice(3, "C")
    g1.add_aresta(0, 1, 1.0, "A->B")
    g1.add_aresta(1, 2, 2.0, "B->C")
    g1.add_aresta(0, 2, 1.5, "A->C")

    g2 = Multigrafo("Grafo 2 (idêntico ao 1)")
    g2.add_vertice(1, "A"); g2.add_vertice(2, "B"); g2.add_vertice(3, "C")
    g2.add_aresta(0, 1, 1.0, "A->B")
    g2.add_aresta(1, 2, 2.0, "B->C")
    g2.add_aresta(0, 2, 1.5, "A->C")

    g1.print_multigrafo()
    g2.print_multigrafo()
    similaridade(g1, g2)

    g3 = Multigrafo("Grafo 3")
    gerar_grafo_aleatorio(g3, num_vertices=5, num_arestas=7)

    g4 = Multigrafo("Grafo 4")
    gerar_grafo_aleatorio(g4, num_vertices=5, num_arestas=7)

    g3.print_multigrafo()
    g4.print_multigrafo()
    similaridade(g3, g4)

    g5 = Multigrafo("Grafo 5")
    g5.add_vertice(1, "A"); g5.add_vertice(2, "B")
    g5.add_vertice(3, "C"); g5.add_vertice(4, "D")
    g5.add_aresta(0, 1, 1.0, "A->B")
    g5.add_aresta(1, 2, 1.0, "B->C")
    g5.add_aresta(2, 3, 1.0, "C->D")
    g5.add_aresta(3, 0, 1.0, "D->A")

    g6 = Multigrafo("Grafo 6 (subconjunto de G5)")
    g6.add_vertice(1, "A"); g6.add_vertice(2, "B")
    g6.add_vertice(3, "C"); g6.add_vertice(4, "D")
    g6.add_aresta(0, 1, 1.0, "A->B")
    g6.add_aresta(1, 2, 1.0, "B->C")

    similaridade(g5, g6)