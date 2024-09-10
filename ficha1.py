# programa para mostrar números impares entre 10 e 34

for num in range(11, 34, 2):
    print(num)
    
    
# Solicita ao usuário um número inteiro positivo menor que 100
numero = int(input("Digite um número inteiro positivo menor que 100: "))

# Verifica se o número está no intervalo permitido
if 0 <= numero < 100:
    dezenas = numero // 10
    unidades = numero % 10
    print(f"O número {numero} tem {dezenas} dezenas e {unidades} unidades.")
else:
    print("O número deve ser um inteiro positivo menor que 100.")



def ler():
    """Lê uma frase do teclado e devolve-a."""
    frase = input("Digite uma frase: ")
    return frase

def gravar(nome_arquivo, frase):
    """Grava uma frase em um ficheiro cujo nome é passado como parâmetro."""
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(frase)

def contaVogais(frase):
    """Recebe uma frase e devolve o número de vogais."""
    vogais = 'aeiouAEIOU'
    contagem = sum(1 for char in frase if char in vogais)
    return contagem

# Leitura das duas frases
print("Digite a primeira frase:")
frase1 = ler()
print("Digite a segunda frase:")
frase2 = ler()

# Contagem de vogais em cada frase
vogais_frase1 = contaVogais(frase1)
vogais_frase2 = contaVogais(frase2)

# Determina qual frase tem mais vogais
if vogais_frase1 > vogais_frase2:
    frase_com_mais_vogais = frase1
    nome_arquivo = "frase_com_mais_vogais1.txt"
else:
    frase_com_mais_vogais = frase2
    nome_arquivo = "frase_com_mais_vogais2.txt"

# Grava a frase com mais vogais no arquivo
gravar(nome_arquivo, frase_com_mais_vogais)

print(f"A frase com mais vogais foi gravada no arquivo {nome_arquivo}.")



def ler_lista():
    """
    Lê uma lista de números inteiros positivos do teclado. A leitura termina quando um número negativo é inserido.
    Retorna a lista de números inteiros positivos.
    """
    lista = []
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo (ou um número negativo para terminar): "))
            if numero < 0:
                break
            lista.append(numero)
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
    return lista

def interseccao_listas(lista1, lista2):
    """
    Recebe duas listas e retorna uma nova lista contendo os números que aparecem em ambas as listas.
    """
    return list(set(lista1) & set(lista2))

def main():
    print("Digite os números para a primeira lista:")
    lista1 = ler_lista()
    print("Digite os números para a segunda lista:")
    lista2 = ler_lista()
    
    resultado = interseccao_listas(lista1, lista2)
    
    print("Os números que aparecem em ambas as listas são:")
    print(resultado)

if __name__ == "__main__":
    main()



import numpy as np

def ler_matriz(mensagem):
    """
    Lê uma matriz 2x2 do teclado.
    """
    matriz = []
    print(mensagem)
    for i in range(2):
        linha = []
        for j in range(2):
            while True:
                try:
                    valor = float(input(f"Digite o valor para a posição ({i+1},{j+1}): "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("Por favor, insira um número válido.")
        matriz.append(linha)
    return np.array(matriz)

def main():
    # Leitura das matrizes
    A = ler_matriz("Digite os valores para a matriz A:")
    B = ler_matriz("Digite os valores para a matriz B:")

    # (a) Produto elemento a elemento A . B
    produto_elemento_a_elemento = A * B
    print("\nProduto elemento a elemento A . B:")
    print(produto_elemento_a_elemento)

    # (b) Produto matricial A * B
    produto_matricial = np.dot(A, B)
    print("\nProduto matricial A * B:")
    print(produto_matricial)

    # (c) Diferença entre matrizes A - B
    diferenca = A - B
    print("\nDiferença entre matrizes A - B:")
    print(diferenca)

    # (d) Logaritmo dos elementos de A (valores absolutos em caso de elementos negativos)
    logaritmo_A = np.log(np.abs(A))
    print("\nLogaritmo dos elementos de A (com valores absolutos):")
    print(logaritmo_A)

    # (e) Maior valor da segunda linha de A vezes o menor valor da primeira coluna de B
    maior_segunda_linha_A = np.max(A[1, :])
    menor_primeira_coluna_B = np.min(B[:, 0])
    resultado = maior_segunda_linha_A * menor_primeira_coluna_B
    print("\nMaior valor da segunda linha de A vezes o menor valor da primeira coluna de B:")
    print(resultado)

if __name__ == "__main__":
    main()



def exibir_menu():
    """
    Exibe o menu de opções para o usuário.
    """
    print("\nMenu:")
    print("1. Inserir novo par UC + nota")
    print("2. Alterar o valor da nota de uma UC")
    print("3. Mostrar todos os pares UC + nota")
    print("4. Mostrar a nota média")
    print("5. Sair")

def inserir_novo(dicionario):
    """
    Insere um novo par UC + nota no dicionário.
    """
    uc = input("Digite o nome da UC: ")
    while True:
        try:
            nota = float(input("Digite a nota da UC (0 a 10): "))
            if 0 <= nota <= 10:
                break
            else:
                print("Nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")
    dicionario[uc] = nota
    print(f"Nota de {uc} inserida com sucesso.")

def alterar_nota(dicionario):
    """
    Altera o valor da nota de uma UC existente no dicionário.
    """
    uc = input("Digite o nome da UC cuja nota deseja alterar: ")
    if uc in dicionario:
        while True:
            try:
                nota = float(input("Digite a nova nota da UC (0 a 10): "))
                if 0 <= nota <= 10:
                    break
                else:
                    print("Nota deve estar entre 0 e 10. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")
        dicionario[uc] = nota
        print(f"Nota de {uc} alterada com sucesso.")
    else:
        print("UC não encontrada.")

def mostrar_pares(dicionario):
    """
    Mostra todos os pares UC + nota armazenados no dicionário.
    """
    if dicionario:
        print("\nPares UC + nota:")
        for uc, nota in dicionario.items():
            print(f"{uc}: {nota}")
    else:
        print("Nenhuma UC registrada.")

def mostrar_media(dicionario):
    """
    Mostra a nota média das UCs armazenadas no dicionário.
    """
    if dicionario:
        media = sum(dicionario.values()) / len(dicionario)
        print(f"\nNota média: {media:.2f}")
    else:
        print("Nenhuma UC registrada para calcular a média.")

def main():
    """
    Função principal que exibe o menu e gerencia as opções do usuário.
    """
    dicionario_uc = {}
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-5): ")
        if opcao == '1':
            inserir_novo(dicionario_uc)
        elif opcao == '2':
            alterar_nota(dicionario_uc)
        elif opcao == '3':
            mostrar_pares(dicionario_uc)
        elif opcao == '4':
            mostrar_media(dicionario_uc)
        elif opcao == '5':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()







def ler_frase(mensagem):
    """
    Lê uma frase do teclado e retorna um conjunto de letras presentes na frase.
    """
    frase = input(mensagem)
    # Remove espaços e converte a frase para minúsculas para garantir consistência
    letras = set(frase.replace(" ", "").lower())
    # Remove caracteres não alfabéticos
    letras = set(c for c in letras if c.isalpha())
    return letras

def main():
    # Ler as duas frases do usuário
    conjunto1 = ler_frase("Digite a primeira frase: ")
    conjunto2 = ler_frase("Digite a segunda frase: ")

    # (a) Todas as letras que aparecem em ambas as frases
    interseccao = conjunto1 & conjunto2
    print("\nLetras que aparecem em ambas as frases:")
    print(interseccao)

    # (b) As letras que aparecem na primeira frase mas não na segunda
    apenas_na_primeira = conjunto1 - conjunto2
    print("\nLetras que aparecem na primeira frase mas não na segunda:")
    print(apenas_na_primeira)

    # (c) As letras que aparecem simultaneamente em ambas as frases
    # (Esta operação é a mesma que a interseção já calculada em (a))
    print("\nLetras que aparecem simultaneamente em ambas as frases:")
    print(interseccao)

    # (d) As letras que só aparecem na primeira frase ou só aparecem na segunda frase
    apenas_uma = conjunto1 ^ conjunto2
    print("\nLetras que aparecem só na primeira frase ou só na segunda frase:")
    print(apenas_uma)

if __name__ == "__main__":
    main()







import networkx as nx

def criar_grafo():
    """
    Cria um grafo representando as principais ligações rodoviárias entre as 18 capitais de distrito de Portugal.
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
    
    # Adiciona as ligações rodoviárias (arestas)
    ligacoes = [
        ("Lisboa", "Porto"), ("Porto", "Aveiro"), ("Aveiro", "Coimbra"), ("Coimbra", "Leiria"), 
        ("Leiria", "Lisboa"), ("Lisboa", "Santarem"), ("Santarem", "Évora"), ("Évora", "Beja"), 
        ("Beja", "Setúbal"), ("Setúbal", "Lisboa"), ("Lisboa", "Braga"), ("Braga", "Guimarães"), 
        ("Guimarães", "Bragança"), ("Bragança", "Vila Real"), ("Vila Real", "Viseu"), ("Viseu", "Castelo Branco"), 
        ("Castelo Branco", "Évora"), ("Évora", "Ponta Delgada"), ("Ponta Delgada", "Funchal")
    ]
    
    G.add_edges_from(ligacoes)
    
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

def main():
    G = criar_grafo()
    listar_vizinhos(G)

if __name__ == "__main__":
    main()

