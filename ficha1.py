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



