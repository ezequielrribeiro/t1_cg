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
        fovy_rad = mth.radians(fovy)
        self.__matriz_proj_perspec = np.matrix(
            [
                [1/(mth.tan(fovy_rad/2)*aspect), 0.0, 0.0, 0.0],
                [0.0, 1/mth.tan(fovy_rad/2), 0.0, 0.0],
                [0.0, 0.0, (z_far+z_near)/(z_near-z_far), (2*z_far*z_near)/(z_near-z_far)],
                [0.0, 0.0, -1, 0.0]
            ]
        )

    def set_matriz_paralela(self, x_left, x_right, y_top, y_bottom, z_near, z_far):
        self.__matriz_proj_paralela = np.matrix(
            [
                [2/(x_right-x_left), 0.0, 0.0, -((x_right+x_left)/(x_right-x_left))],
                [0.0, 2/(y_top-y_bottom), 0.0, -((y_top+y_bottom)/(y_top-y_bottom))],
                [0.0, 0.0, -(2/(z_far-z_near)), -((z_far+z_near)/(z_far-z_near))],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )

    def get_pontos_perspectiva(self):
        perspectiva_2d = []
        for ponto in self.__lista_pontos:
            temp = self.__matriz_proj_perspec * ponto.get_matriz_coluna()
            ponto_2d = [round(temp.item(0, 0)/temp.item(3, 0), 2), round(temp.item(1, 0)/temp.item(3, 0), 2)]
            perspectiva_2d.append(ponto_2d)
        return perspectiva_2d

    def get_pontos_paralela(self):
        paralela_2d = []
        for ponto in self.__lista_pontos:
            temp = self.__matriz_proj_paralela * ponto.get_matriz_coluna()
            ponto_2d = [round(temp.item(0, 0)/temp.item(3, 0), 2), round(temp.item(1, 0)/temp.item(3, 0), 2)]
            paralela_2d.append(ponto_2d)
        return paralela_2d