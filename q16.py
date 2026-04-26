from q5 import Multigrafo, gerar_grafo_aleatorio
from collections import deque

def grafo_para_nao_dirigido(grafo):
    adj = {}
    for v in grafo.vertices:
        if v.is_active:
            adj[v.vertice_id] = set()

    for v in grafo.vertices:
        if v.is_active:
            for aresta in grafo.iterar_aresta(v.cabeca_arestas):
                d = aresta.dest_id
                if grafo.vertices[d].is_active and d != v.vertice_id:
                    adj[v.vertice_id].add(d)
                    adj[d].add(v.vertice_id)
    return adj


def componentes_conexas(adj):
    visitado = set()
    componentes = []
    for v in adj:
        if v not in visitado:
            comp = set()
            fila = deque([v])
            visitado.add(v)
            while fila:
                u = fila.popleft()
                comp.add(u)
                for w in adj[u]:
                    if w not in visitado:
                        visitado.add(w)
                        fila.append(w)
            componentes.append(comp)
    return componentes


def euler_necessario(V, E, cintura=3):
    if V < 3:
        return True
    if cintura >= 4:
        return E <= 2 * V - 4
    return E <= 3 * V - 6


def tem_k5_ou_k33(adj, vertices):
    vlist = list(vertices)
    n = len(vlist)

    if n >= 5:
        from itertools import combinations
        for combo in combinations(vlist, 5):
            k5 = True
            for i in range(5):
                for j in range(i+1, 5):
                    if combo[j] not in adj[combo[i]]:
                        k5 = False
                        break
                if not k5:
                    break
            if k5:
                return True, "K5", combo

    if n >= 6:
        from itertools import combinations, permutations
        for combo in combinations(vlist, 6):
            for split in combinations(range(6), 3):
                A = [combo[i] for i in split]
                B = [combo[i] for i in range(6) if i not in split]
                k33 = all(b in adj[a] for a in A for b in B)
                if k33:
                    return True, "K3,3", (A, B)

    return False, None, None


def verificar_planaridade(grafo):
    adj = grafo_para_nao_dirigido(grafo)
    vertices = [v.vertice_id for v in grafo.vertices if v.is_active]
    V = len(vertices)

    arestas_nd = set()
    for u in adj:
        for v in adj[u]:
            arestas_nd.add((min(u, v), max(u, v)))
    E = len(arestas_nd)

    if V == 0:
        return True, "Grafo vazio: trivialmente planar."
    if V <= 2:
        return True, f"Grafo com {V} vértice(s): trivialmente planar."

    comps = componentes_conexas(adj)

    for comp in comps:
        e_comp = sum(1 for (u, v) in arestas_nd if u in comp and v in comp)
        v_comp = len(comp)
        if not euler_necessario(v_comp, e_comp):
            return False, (
                f"Viola condição de Euler: componente com V={v_comp}, E={e_comp}. "
                f"E > 3V-6 = {3*v_comp-6}. Definitivamente não-planar."
            )

    if V <= 10:
        encontrou, tipo, partes = tem_k5_ou_k33(adj, vertices)
        if encontrou:
            return False, f"Contém {tipo} como subgrafo: não-planar (Kuratowski)."
        return True, (
            f"Satisfaz condição de Euler (V={V}, E={E}, E ≤ {3*V-6}) "
            f"e não contém K5 nem K3,3 como subgrafo direto: planar."
        )
    else:
        return None, (
            f"V={V} > 10: condição de Euler satisfeita (E={E} ≤ {3*V-6}), "
            "mas verificação completa de subdivisões de K5/K3,3 requer "
            "algoritmo de Boyer-Myrvold (não implementado aqui para V grandes)."
        )


def print_planaridade(grafo):
    grafo.print_multigrafo()
    resultado, justificativa = verificar_planaridade(grafo)
    print(f"\nGrafo: {grafo.name}")
    if resultado is True:
        print(f"  ✔ PLANAR: {justificativa}")
    elif resultado is False:
        print(f"  ✘ NÃO PLANAR: {justificativa}")
    else:
        print(f"  ? INCONCLUSIVO: {justificativa}")
    return resultado


if __name__ == "__main__":
    g1 = Multigrafo("K4 (planar)")
    for i in range(4): g1.add_vertice(i, f"V{i}")
    edges_k4 = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    for (u,v) in edges_k4:
        g1.add_aresta(u, v, 1.0, f"{u}->{v}")
        g1.add_aresta(v, u, 1.0, f"{v}->{u}")
    print("=== K4 ===")
    print_planaridade(g1)

    g2 = Multigrafo("K5 (não planar)")
    for i in range(5): g2.add_vertice(i, f"V{i}")
    from itertools import combinations
    for (u,v) in combinations(range(5), 2):
        g2.add_aresta(u, v, 1.0, f"{u}->{v}")
        g2.add_aresta(v, u, 1.0, f"{v}->{u}")
    print("\n=== K5 ===")
    print_planaridade(g2)

    g3 = Multigrafo("K3,3 (não planar)")
    for i in range(6): g3.add_vertice(i, f"V{i}")
    for a in [0,1,2]:
        for b in [3,4,5]:
            g3.add_aresta(a, b, 1.0, f"{a}->{b}")
            g3.add_aresta(b, a, 1.0, f"{b}->{a}")
    print("\n=== K3,3 ===")
    print_planaridade(g3)

    g4 = Multigrafo("Grafo aleatório (5 vértices, 6 arestas)")
    gerar_grafo_aleatorio(g4, num_vertices=5, num_arestas=6)
    print("\n=== Grafo Aleatório ===")
    print_planaridade(g4)

    g5 = Multigrafo("C5 - ciclo de 5 (planar)")
    for i in range(5): g5.add_vertice(i, f"V{i}")
    for i in range(5):
        g5.add_aresta(i, (i+1)%5, 1.0, f"{i}->{(i+1)%5}")
        g5.add_aresta((i+1)%5, i, 1.0, f"{(i+1)%5}->{i}")
    print("\n=== C5 ===")
    print_planaridade(g5)