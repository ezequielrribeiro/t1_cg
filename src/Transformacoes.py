from numpy import *


class Matriz_Quadrada:
    def __init__(self, dim=4):
        self.__dimensao = dim
        if self.__dimensao == 4:
            self.__matriz = self.identidade()

    def get_dimensao(self):
        return self.__dimensao

    @property
    def __identidade(self):
        m = array(
            [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        return m

    @property
    def __vazia(self):
        m = array(
            [
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0],
                [0.0, 0.0, 0.0, 0.0]
            ]
        )
        return m

    def get_elemento(self, linha, coluna):
        return self.__matriz[linha][coluna]

    def set_elemento(self, linha, coluna, valor=0.0):
        self.__matriz[linha][coluna] = valor

    def multiplica(self, matriz):
        if self.__dimensao == matriz.get_dimensao():
            m = self.__vazia()


