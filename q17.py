from q5 import Multigrafo, gerar_grafo_aleatorio
from q7 import posorder

Multigrafo.posorder = posorder

if __name__ == "__main__":
    g1 = Multigrafo("Grafo 1")
    gerar_grafo_aleatorio(g1, 5, 5)
    g1.print_multigrafo()

    print(f"Rotulação Topológica do Grafo: {posorder(g1)}")
    # Função de rotulação topológica é a mesma que a ordenação topológica, então reutilizamos o código do q7 para isso.