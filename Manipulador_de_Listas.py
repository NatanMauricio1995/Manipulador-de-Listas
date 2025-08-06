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
