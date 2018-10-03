import copy
import math as mth
import numpy as np

class Projecao:

    def __init__(self, pontos):
        self.__matriz_proj_perspec = None
        self.__matriz_proj_paralela = None
        self.__lista_pontos = []
        for ponto in pontos:
            self.__lista_pontos.append(copy.copy(ponto))

    def set_matriz_perspectiva(self, fovy, aspect, z_near, z_far):
        self.__matriz_proj_perspec = np.matrix(
            [
                [1/(mth.tan(fovy/2)*aspect), 0.0, 0.0, 0.0],
                [0.0, 1/mth.tan(fovy/2), 0.0, 0.0],
                [0.0, 0.0, (z_far+z_near)/(z_near-z_far), (2*z_far*z_near)/(z_near-z_far)],
                [0.0, 0.0, -1, 0.0]
            ]
        )

    #def aplicar_perspectiva(self):
