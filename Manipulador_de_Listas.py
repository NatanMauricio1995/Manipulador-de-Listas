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
