import numpy as np

class Ponto:
    """
    Classe usada para representação e manipulação de um ponto no espaço R3(x, y, z)
    """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        """
        Inicialização da classe. Seta como padrão as coordenadas em 0.0,
        caso não sejam setadas.
        :param x: valor da coordenada x
        :param y: valor da coordenada y
        :param z: valor da coordenada z
        """
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        """
        Obter o valor da coordenada x do ponto
        :return: float
        """
        return self.__x

    def get_y(self):
        """
        Obter o valor da coordenada y do ponto
        :return: float
        """
        return self.__y

    def get_z(self):
        """
        Obter o valor da coordenada z do ponto
        :return: float
        """
        return self.__z

    def set_x(self, x):
        """
        Definir o valor da coordenada x do ponto em R3
        :param x: valor de x (float)
        :return: void
        """
        self.__x = x

    def set_y(self, y):
        """
        Definir o valor da coordenada y do ponto em R3
        :param y: valor de y (float)
        :return: void
        """
        self.__y = y

    def set_z(self, z):
        """
        Definir o valor da coordenada z do ponto em R3
        :param z: valor de z (float)
        :return: void
        """
        self.__z = z

    def get_matriz_coluna(self) -> np.matrix:
        """
        Retorna o ponto em R3 no formato de matriz coluna, com coordenada homogênea
        :return: matriz coluna do tipo matrix
        """
        return np.matrix(
            [
                [self.__x],
                [self.__y],
                [self.__z],
                [1]
            ]
        )
