import numpy as np

class Ponto:

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.__x = x
        self.__y = y
        self.__z = z

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_z(self, z):
        self.__z = z

    def get_matriz_coluna(self) -> np.matrix:
        return np.matrix(
            [
                [self.__x],
                [self.__y],
                [self.__z],
                [1]
            ]
        )
