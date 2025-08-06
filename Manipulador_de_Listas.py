# Manipulador de Listas em Python

Sistema interativo para manipulação de listas de números inteiros com interface de menu, desenvolvido aplicando conceitos de Programação Orientada a Objetos e tratamento de erros.

**Funcionalidades:**
- Adicionar e remover elementos
- Calcular maior, menor e média dos valores
- Interface visual com validação de entrada
- Navegação por menu interativo

**Autor:** Natan Mauricio Santos  
**Contato:** natanmauriciosantos@hotmail.com  
**GitHub:** [github.com/NatanMauricio1995](https://github.com/NatanMauricio1995)

"""
--------------
CLASSE
--------------
"""
#Cria a classe lista
class ManipuladorDeLista:
    
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
        maior = max(self.lista)
        return maior
    
    #Encontra e retorna o menor elemento da lista
    def encontrar_menor(self):
        menor = min(self.lista)
        return menor
    
    #Calcula e retorna a média dos elementos na lista
    def calcular_media(self):
        #Calcula quantos elementos a lista possui
        quantidade_de_elementos = len(self.lista) 
        
        #Soma todos os elementos da lista
        soma_dos_elementos = sum(self.lista)
        
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
#Capta o valor numérico esperado e 
def ler_numero(pergunta, condicao, retorno_positivo, retorno_negativo):
    while True:
        try:
            numero = int(input(pergunta))
            if(condicao(numero)):
                print(retorno_positivo)
                
                #Imprime um delimitador visual
                delimitador_visual()
                
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
def continuar():
    #Zera o parâmetro
    numero = 0
    
    #Loop para garantir a repetição
    while ((numero != 2) and (numero != 1)):
        #Imprime as opções
        print("Deseja inserir novos números à lista?")
        print("     1. Sim")
        print("     2. Não")
        numero = ler_numero(
            "Insira o valor da opção escolhida:",
            lambda opcao:((opcao == 1) or (opcao == 2)),
            "Escolha recebida!",
            "Insira '1' para SIM e '2' para NÃO!"
        )
    
    return numero

#Função main
def main():
    
    manipulador = ManipuladorDeLista()
    
    #Zera o parâmetro
    escolha = 0
    
    #Loop para o menu
    while (escolha != 7):
        menu()
        escolha = ler_numero(
            "Insira o valor numérico da sua escolha: ",
            lambda opcao:((opcao >= 1) and (opcao <= 7)),
            "Escolha recebida!",
            "Insira um valor numérico válido!"            
        )
        
        #Chama a função que adiciona um elemento na lista
        if(escolha == 1):
            adicionar(manipulador)
            
        #Chama a função que remove um elemento na lista 
        elif(escolha == 2):
            remover(manipulador)
            
        #Chama a função que exibe o maior valor da lista
        elif(escolha == 3):
            maior_elemento(manipulador)
            
        #Chama a função que exibe o menor valor da lista
        elif(escolha == 4):
            menor_elemento(manipulador)
            
        #Chama a função que exibe média de valores da lista
        elif(escolha == 5):
            media_elementos(manipulador) 
            
        #Chama a função que exibe todos os elementos da lista
        elif(escolha == 6):
            exibir_lista(manipulador)
            
        elif(escolha == 7):
            sair()
    
#Função que avalia se a lista está vazia
def lista_vazia(manipulador):
    quantidade_elementos = len(manipulador.lista)
    if (quantidade_elementos == 0):
        print("A lista está vazia!")
        return 0
    else:
        return 1
            
"""
--------------
FUNÇÕES DAS OPÇÕES
--------------    
"""
#Função que insere o número na lista
def adicionar(manipulador):
    
    repetir = 1
    
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("ADICIONAR UM ELEMENTO NO FINAL DA LISTA")
    
    while (repetir != 2):

        #Imprime o título
        imprime_titulo(titulo, quantidade_espacos)
        
        #Lê o número a ser adicionado
        numero = ler_numero(
            "Insira o valor a ser adicionado à lista: ",
            lambda  entrada: isinstance (entrada, int),
            "O valor foi adicionado com sucesso!",
            "Por gentileza insira um valor numérico!"
        )

        #Insere o número na lista
        manipulador.adicionar_elemento(numero)
        
        #Verifica se o usuário quer repetir o procedimento
        repetir = continuar()
        
    delimitador_visual()
    

def remover(manipulador):
    repetir = 1
    
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("REMOVER UM ELEMENTO DA LISTA")
    
    while (repetir != 2):

        #Imprime o título
        imprime_titulo(titulo, quantidade_espacos)
        
        #Lê o número a ser removido
        numero = ler_numero(
            "Insira o valor a ser removido da lista: ",
            lambda entrada: entrada in manipulador.lista,
            "O valor foi removido com sucesso!",
            "O valor inserido não está na lista"
        )

        #Remove o número na lista
        manipulador.remover_elemento(numero)
        
        #Verifica se o usuário quer repetir o procedimento
        repetir = continuar()
        
    delimitador_visual()
    
#Função que exibe o maior valor
def maior_elemento(manipulador):
    
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("EXIBIR O MAIOR VALOR DA LISTA")
    
    #Imprime o título
    imprime_titulo(titulo, quantidade_espacos)
    
    #Teste se a lista está vazia
    teste = lista_vazia(manipulador)
    
    if(teste == 1):
        print(f"O maior valor da lista é: {manipulador.encontrar_maior()}")
   
    delimitador_visual()
    
#Função que exibe o menor valor
def menor_elemento(manipulador):
    
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("EXIBIR O MENOR VALOR DA LISTA")
    
    #Imprime o título
    imprime_titulo(titulo, quantidade_espacos)
    
    #Teste se a lista está vazia
    teste = lista_vazia(manipulador)
    
    if(teste == 1):
        print(f"O menor valor da lista é: {manipulador.encontrar_menor()}")
   
    delimitador_visual()
    
#Função que exibe a média
def media_elementos(manipulador):
    
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("EXIBIR A MÉDIA DA LISTA")
    
    #Imprime o título
    imprime_titulo(titulo, quantidade_espacos)
    
    #Teste se a lista está vazia
    teste = lista_vazia(manipulador)
    
    if(teste == 1):  
        print(f"A média da lista é: {manipulador.calcular_media():.3f}")

        
    delimitador_visual()
        
#Função que exibe a lista:
def exibir_lista(manipulador):
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("EXIBIR A LISTA COMPLETA")
    
    #Imprime o título
    imprime_titulo(titulo, quantidade_espacos)
    
    #Teste se a lista está vazia
    teste = lista_vazia(manipulador)
    
    if(teste == 1):  
        manipulador.mostrar_lista()
    
    delimitador_visual()


#Exibe despedida
def sair():
    
    #Ajuste do título
    titulo, quantidade_espacos = configura_titulo("Muito obrigado! Até mais!")
    
    #Imprime o título
    imprime_titulo(titulo, quantidade_espacos)
    
if __name__ == "__main__":
    main()
