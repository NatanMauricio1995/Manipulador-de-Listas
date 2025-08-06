"""
--------------
CLASSE
--------------
"""
#Cria a classe lista
class Manipulador_de_Lista:
    
    #Cria o método contrutor da classe
    def __init__(self):
        self.lista = []

    #Adiciona um elemento no final da lista
    def adicionar_elemento(self,elemento):
        self.lista.append(elemento)

    #Remove a primeira ocorrência do elemento na lista
    def remover_elemento(self, elemento):
        self.lista.remove(elemento)
        
    #Encontra e retorna o maior elemento da lista
    def encontrar_maior(self):
        maior = self.lista.max()
        return = maior

    #Encontra e retorna o menor elemento da lista
    def encontrar_menor(self):
        menor = self.lista.min()
        return menor

    #Calcula e retorna a média dos elementos na lista
    def calcular_media(self):
        #Calcula quantos elementos a lista possui
        quantidade_de_elementos = len(self.lista) 
        
        #Soma todos os elementos da lista
        soma_dos_elementos = self.lista.sum()
        
        #Calcula a média dos elementos
        media = soma_dos_elementos / quantidade_de_elementos
        
        return media

    #Retorna a lista atual
    def mostrar_lista(self):
        print(f"Lista = {self.lista}")

"""
--------------
LAYOUT DA TELA
--------------
"""
#Define globalmente a quantidade de traços
quantidade_tracos = 100

#Configura o título da sessão
def configura_titulo(titulo):
    
    #Transforma o título em letras maiúsculas
    titulo = titulo.upper()
    
    #Determina o tamanho do título
    tamanho_titulo = len(titulo)
    
    #Calcula a quantidade de espaços para que o título esteja centralizado na tela
    quantidade_espacos = (quantidade_tracos - tamanho_titulo) // 2
    
    return titulo, quantidade_espacos

#Imprime o delimitador visual
def delimitador_visual():
    print("-" * quantidade_tracos)

#Imprime título
def imprime_titulo(titulo, quantidade_espacos):
    print()
    delimitador_visual()
    print(" " * quantidade_espacos, titulo)
    delimitador_visual()
    print()
"""
--------------
TRATAMENTO DE ERROS
--------------
"""
#Capta o valor numérico esperado e verifica a entrada
def ler_numeros(pergunta, condicao, retorno_positivo, retorno_negativo):
    while True:
        try:
            numero = int(input(pergunta))
            if(condicao(numero)):
                print(retorno_positivo)
                return numero
            else:
                print(retorno_negativo)
        except ValueError:
            print("Por gentileza insira um valor numérico inteiro!")

"""
--------------
FUNÇÕES GERAIS
--------------    
"""
#Imprime o menu principal
def menu():
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("Menu")
	
    #Imprime o título
    imprime_titulo(titulo, quantidade_espacos)
    
    #Imprime as opções
    print("Opções:")
    print("     1. Adicionar um elemento no final da lista;")
    print("     2. Remover a primeira ocorrência do elemento na lista;")
    print("     3. Exibir o maior valor da lista;")
    print("     4. Exibir o menor valor da lista;")
    print("     5. Calcular média dos elementos da lista;")
    print("     6. Exibir lista;")
    print("     7. Sair.")
	
    #Imprime um delimitador visual
    delimitador_visual()
	
#Define escolha de continuar
def coninuar():
    #Zera o parâmetro
    numero = 0
    
    #Loop para garantir a repetição
    while (numero != 2):
        #Imprime as opções
        print("Deseja inserir novos números à lista?")
        print("     1. Sim")
        print("     2. Não")
        numero = ler_numeros(
            "Insira o valor da opção escolhida:",
            lambda x:((x == 1) or (x == 2)),
            "Escolha recebida!",
            "Insira '1' para SIM e '2' para NÃO!"
        )
    
    return numero
