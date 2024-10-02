import networkx as nx
'''
def criar_grafo():
    """
    Cria um grafo representando as principais ligações rodoviárias entre as 18 capitais de distrito de Portugal,
    com as distâncias em Km.
    """
    # Criação do grafo não dirigido
    G = nx.Graph()

    # Lista das capitais de distrito
    capitais = [
        "Lisboa", "Porto", "Aveiro", "Braga", "Viana do Castelo", "Guimarães", "Bragança", "Vila Real", 
        "Ponta Delgada", "Funchal", "Coimbra", "Leiria", "Santarem", "Évora", "Beja", "Setúbal", 
        "Castelo Branco", "Viseu"
    ]
    
    # Adiciona as capitais como nós no grafo
    G.add_nodes_from(capitais)
    
    # Adiciona as ligações rodoviárias (arestas) com as distâncias em km
    ligacoes = [
        ("Lisboa", "Porto", 313), ("Porto", "Aveiro", 75), ("Aveiro", "Coimbra", 62), 
        ("Coimbra", "Leiria", 71), ("Leiria", "Lisboa", 143), ("Lisboa", "Santarem", 84), 
        ("Santarem", "Évora", 108), ("Évora", "Beja", 79), ("Beja", "Setúbal", 142), 
        ("Setúbal", "Lisboa", 50), ("Lisboa", "Braga", 364), ("Braga", "Guimarães", 25), 
        ("Guimarães", "Bragança", 192), ("Bragança", "Vila Real", 139), ("Vila Real", "Viseu", 88), 
        ("Viseu", "Castelo Branco", 141), ("Castelo Branco", "Évora", 223), 
        ("Évora", "Ponta Delgada", 0),  # A ligação entre ilhas não faz sentido, mas mantemos a conexão
        ("Ponta Delgada", "Funchal", 0)  # para simplificação da topologia
    ]
    
    # Adiciona as ligações com pesos (distâncias)
    for cidade1, cidade2, distancia in ligacoes:
        G.add_edge(cidade1, cidade2, weight=distancia)
    
    return G

def listar_vizinhos(G):
    """
    Lista para cada cidade do mapa o conjunto das suas cidades vizinhas.
    """
    for cidade in G.nodes():
        vizinhos = list(G.neighbors(cidade))
        print(f"Cidade: {cidade}")
        print(f"Cidades vizinhas: {', '.join(vizinhos)}")
        print()

def comprimento(G, caminho):
    """
    Calcula o comprimento total de um caminho no grafo, dado por uma lista de nodos.
    """
    total_km = 0
    for i in range(len(caminho) - 1):
        cidade1 = caminho[i]
        cidade2 = caminho[i + 1]
        
        if G.has_edge(cidade1, cidade2):
            total_km += G[cidade1][cidade2]['weight']
        else:
            print(f"Caminho inválido: não existe uma ligação direta entre {cidade1} e {cidade2}.")
            return None
    return total_km

def main():
    # Criar o grafo com as capitais e suas conexões
    G = criar_grafo()

    # Listar os vizinhos para ver como está estruturado o grafo
    listar_vizinhos(G)

    # Pedir ao utilizador para inserir um caminho
    caminho = input("Digite um caminho (lista de capitais separadas por vírgulas): ").split(",")

    # Remover espaços em branco nas entradas
    caminho = [cidade.strip() for cidade in caminho]

    # Calcular o comprimento do caminho
    total_distancia = comprimento(G, caminho)

    if total_distancia is not None:
        print(f"O comprimento total do caminho é: {total_distancia} km.")
    else:
        print("O caminho fornecido é inválido.")

if __name__ == "__main__":
    main()

'''
# exercicio 2
'''
import networkx as nx
from networkx.algorithms import bfs_edges

def criar_grafo():
    """
    Cria um grafo representando as principais ligações rodoviárias entre as 18 capitais de distrito de Portugal,
    com as distâncias em Km.
    """
    G = nx.Graph()

    capitais = [
        "Lisboa", "Porto", "Aveiro", "Braga", "Viana do Castelo", "Guimarães", "Bragança", "Vila Real", 
        "Ponta Delgada", "Funchal", "Coimbra", "Leiria", "Santarem", "Évora", "Beja", "Setúbal", 
        "Castelo Branco", "Viseu"
    ]
    
    G.add_nodes_from(capitais)
    
    ligacoes = [
        ("Lisboa", "Porto", 313), ("Porto", "Aveiro", 75), ("Aveiro", "Coimbra", 62), 
        ("Coimbra", "Leiria", 71), ("Leiria", "Lisboa", 143), ("Lisboa", "Santarem", 84), 
        ("Santarem", "Évora", 108), ("Évora", "Beja", 79), ("Beja", "Setúbal", 142), 
        ("Setúbal", "Lisboa", 50), ("Lisboa", "Braga", 364), ("Braga", "Guimarães", 25), 
        ("Guimarães", "Bragança", 192), ("Bragança", "Vila Real", 139), ("Vila Real", "Viseu", 88), 
        ("Viseu", "Castelo Branco", 141), ("Castelo Branco", "Évora", 223), 
        ("Évora", "Ponta Delgada", 0), ("Ponta Delgada", "Funchal", 0)
    ]
    
    for cidade1, cidade2, distancia in ligacoes:
        G.add_edge(cidade1, cidade2, weight=distancia)
    
    return G

def comprimento(G, caminho):
    """
    Calcula o comprimento total de um caminho no grafo, dado por uma lista de nodos.
    """
    total_km = 0
    for i in range(len(caminho) - 1):
        cidade1 = caminho[i]
        cidade2 = caminho[i + 1]
        
        if G.has_edge(cidade1, cidade2):
            total_km += G[cidade1][cidade2]['weight']
        else:
            print(f"Caminho inválido: não existe uma ligação direta entre {cidade1} e {cidade2}.")
            return None
    return total_km

def encontrar_caminho_bfs(G, partida, destino):
    """
    Usa a Pesquisa Primeiro em Largura (PPL) para encontrar o caminho entre a cidade de partida e a cidade de destino.
    Retorna o caminho como uma lista de cidades.
    """
    # Obtenha a lista de arestas da BFS
    arestas_bfs = list(bfs_edges(G, source=partida))

    # Constrói o caminho a partir da lista de arestas
    caminho = [partida]
    for u, v in arestas_bfs:
        caminho.append(v)
        if v == destino:
            break
    
    return caminho if caminho[-1] == destino else None

def main():
    # Criar o grafo
    G = criar_grafo()

    # Pedir ao utilizador para inserir a cidade de partida e destino
    partida = input("Digite a cidade de partida: ").strip()
    destino = input("Digite a cidade de destino: ").strip()

    # Encontrar o caminho usando BFS
    caminho = encontrar_caminho_bfs(G, partida, destino)

    if caminho:
        # Mostrar o caminho
        print(f"Caminho encontrado: {' -> '.join(caminho)}")

        # Calcular e mostrar o comprimento total do caminho
        total_distancia = comprimento(G, caminho)
        print(f"O comprimento total do caminho é: {total_distancia} km.")
    else:
        print(f"Não foi possível encontrar um caminho entre {partida} e {destino}.")

if __name__ == "__main__":
    main()
'''

# exercicio 3
''''
import networkx as nx
from networkx.algorithms.shortest_paths.astar import astar_path

def criar_grafo():
    """
    Cria um grafo representando as principais ligações rodoviárias entre as 18 capitais de distrito de Portugal,
    com as distâncias em Km.
    """
    G = nx.Graph()

    capitais = [
        "Lisboa", "Porto", "Aveiro", "Braga", "Viana do Castelo", "Guimarães", "Bragança", "Vila Real", 
        "Ponta Delgada", "Funchal", "Coimbra", "Leiria", "Santarem", "Évora", "Beja", "Setúbal", 
        "Castelo Branco", "Viseu"
    ]
    
    G.add_nodes_from(capitais)
    
    ligacoes = [
        ("Lisboa", "Porto", 313), ("Porto", "Aveiro", 75), ("Aveiro", "Coimbra", 62), 
        ("Coimbra", "Leiria", 71), ("Leiria", "Lisboa", 143), ("Lisboa", "Santarem", 84), 
        ("Santarem", "Évora", 108), ("Évora", "Beja", 79), ("Beja", "Setúbal", 142), 
        ("Setúbal", "Lisboa", 50), ("Lisboa", "Braga", 364), ("Braga", "Guimarães", 25), 
        ("Guimarães", "Bragança", 192), ("Bragança", "Vila Real", 139), ("Vila Real", "Viseu", 88), 
        ("Viseu", "Castelo Branco", 141), ("Castelo Branco", "Évora", 223), 
        ("Évora", "Ponta Delgada", 0), ("Ponta Delgada", "Funchal", 0)
    ]
    
    for cidade1, cidade2, distancia in ligacoes:
        G.add_edge(cidade1, cidade2, weight=distancia)
    
    return G

def comprimento(G, caminho):
    """
    Calcula o comprimento total de um caminho no grafo, dado por uma lista de nodos.
    """
    total_km = 0
    for i in range(len(caminho) - 1):
        cidade1 = caminho[i]
        cidade2 = caminho[i + 1]
        
        if G.has_edge(cidade1, cidade2):
            total_km += G[cidade1][cidade2]['weight']
        else:
            print(f"Caminho inválido: não existe uma ligação direta entre {cidade1} e {cidade2}.")
            return None
    return total_km

def encontrar_caminho_a_estrela(G, partida, destino):
    """
    Usa a Pesquisa A* para encontrar o caminho mais curto entre a cidade de partida e a cidade de destino.
    Retorna o caminho como uma lista de cidades.
    """
    try:
        caminho = astar_path(G, partida, destino, heuristic=None, weight='weight')
        return caminho
    except nx.NetworkXNoPath:
        return None

def main():
    # Criar o grafo
    G = criar_grafo()

    # Pedir ao utilizador para inserir a cidade de partida e destino
    partida = input("Digite a cidade de partida: ").strip()
    destino = input("Digite a cidade de destino: ").strip()

    # Encontrar o caminho usando A*
    caminho = encontrar_caminho_a_estrela(G, partida, destino)

    if caminho:
        # Mostrar o caminho
        print(f"Caminho encontrado: {' -> '.join(caminho)}")

        # Calcular e mostrar o comprimento total do caminho
        total_distancia = comprimento(G, caminho)
        print(f"O comprimento total do caminho é: {total_distancia} km.")
    else:
        print(f"Não foi possível encontrar um caminho entre {partida} e {destino}.")

if __name__ == "__main__":
    main()
''''
''''
#exercicio 4
import networkx as nx
from networkx.algorithms import bfs_edges, astar_path

def criar_grafo():
    """
    Cria um grafo representando as principais ligações rodoviárias entre as 18 capitais de distrito de Portugal,
    com as distâncias em Km.
    """
    G = nx.Graph()

    capitais = [
        "Lisboa", "Porto", "Aveiro", "Braga", "Viana do Castelo", "Guimarães", "Bragança", "Vila Real", 
        "Ponta Delgada", "Funchal", "Coimbra", "Leiria", "Santarem", "Évora", "Beja", "Setúbal", 
        "Castelo Branco", "Viseu"
    ]
    
    G.add_nodes_from(capitais)
    
    ligacoes = [
        ("Lisboa", "Porto", 313), ("Porto", "Aveiro", 75), ("Aveiro", "Coimbra", 62), 
        ("Coimbra", "Leiria", 71), ("Leiria", "Lisboa", 143), ("Lisboa", "Santarem", 84), 
        ("Santarem", "Évora", 108), ("Évora", "Beja", 79), ("Beja", "Setúbal", 142), 
        ("Setúbal", "Lisboa", 50), ("Lisboa", "Braga", 364), ("Braga", "Guimarães", 25), 
        ("Guimarães", "Bragança", 192), ("Bragança", "Vila Real", 139), ("Vila Real", "Viseu", 88), 
        ("Viseu", "Castelo Branco", 141), ("Castelo Branco", "Évora", 223), 
        ("Évora", "Ponta Delgada", 0), ("Ponta Delgada", "Funchal", 0)
    ]
    
    for cidade1, cidade2, distancia in ligacoes:
        G.add_edge(cidade1, cidade2, weight=distancia)
    
    return G

def comprimento(G, caminho):
    """
    Calcula o comprimento total de um caminho no grafo, dado por uma lista de nodos.
    """
    total_km = 0
    for i in range(len(caminho) - 1):
        cidade1 = caminho[i]
        cidade2 = caminho[i + 1]
        
        if G.has_edge(cidade1, cidade2):
            total_km += G[cidade1][cidade2]['weight']
        else:
            print(f"Caminho inválido: não existe uma ligação direta entre {cidade1} e {cidade2}.")
            return None
    return total_km

def encontrar_caminho_bfs(G, partida, destino):
    """
    Usa a Pesquisa Primeiro em Largura (PPL) para encontrar o caminho entre a cidade de partida e a cidade de destino.
    Retorna o caminho como uma lista de cidades.
    """
    # Obtenha a lista de arestas da BFS
    arestas_bfs = list(bfs_edges(G, source=partida))

    # Constrói o caminho a partir da lista de arestas
    caminho = [partida]
    for u, v in arestas_bfs:
        caminho.append(v)
        if v == destino:
            break
    
    return caminho if caminho[-1] == destino else None

def encontrar_caminho_a_estrela(G, partida, destino):
    """
    Usa a Pesquisa A* para encontrar o caminho mais curto entre a cidade de partida e a cidade de destino.
    Retorna o caminho como uma lista de cidades.
    """
    try:
        caminho = astar_path(G, partida, destino, heuristic=None, weight='weight')
        return caminho
    except nx.NetworkXNoPath:
        return None

def comparar_metodos(G, problemas):
    """
    Compara as distâncias encontradas por BFS e A* para diferentes pares de cidades.
    """
    resultados = []

    for i, (partida, destino) in enumerate(problemas, start=1):
        print(f"Experiência {i}: {partida} -> {destino}")

        # BFS
        caminho_bfs = encontrar_caminho_bfs(G, partida, destino)
        distancia_bfs = comprimento(G, caminho_bfs) if caminho_bfs else None

        # A*
        caminho_a_estrela = encontrar_caminho_a_estrela(G, partida, destino)
        distancia_a_estrela = comprimento(G, caminho_a_estrela) if caminho_a_estrela else None

        # Registrar resultados
        resultados.append((distancia_bfs, distancia_a_estrela))

        print(f"PPL: {distancia_bfs} km, A*: {distancia_a_estrela} km\n")
    
    return resultados

def calcular_media(resultados):
    """
    Calcula a média das distâncias para ambos os métodos.
    """
    total_bfs = 0
    total_a_estrela = 0
    n = len(resultados)

    for bfs, a_estrela in resultados:
        if bfs is not None:
            total_bfs += bfs
        if a_estrela is not None:
            total_a_estrela += a_estrela

    media_bfs = total_bfs / n
    media_a_estrela = total_a_estrela / n

    return media_bfs, media_a_estrela

def main():
    # Criar o grafo
    G = criar_grafo()

    # Definir 10 problemas (pares de cidades)
    problemas = [
        ("Faro", "Bragança"), ("Beja", "Lisboa"), ("Porto", "Setúbal"), ("Coimbra", "Guimarães"), 
        ("Évora", "Viseu"), ("Aveiro", "Braga"), ("Santarem", "Castelo Branco"), ("Lisboa", "Bragança"), 
        ("Braga", "Beja"), ("Leiria", "Porto")
    ]

    # Comparar os métodos
    resultados = comparar_metodos(G, problemas)

    # Calcular e mostrar as médias
    media_bfs, media_a_estrela = calcular_media(resultados)
    print(f"Média PPL: {media_bfs} km, Média A*: {media_a_estrela} km")

if __name__ == "__main__":
    main()
''''
