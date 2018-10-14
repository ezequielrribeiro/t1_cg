import copy
import math as mth
import numpy as np

class Projecao:
    """
    Classe responsável por aplicar transformação nos pontos do objeto para reduzir
    a dimensão do espaço R3 para o espaço R2(presente nos monitores, telas, etc).
    Aplica as projeções do tipo perspectiva e paralela.    """

    def __init__(self, pontos=[]):
        self.__matriz_proj_perspec = None
        self.__matriz_proj_paralela = None
        self.__lista_pontos = pontos

    def set_lista_pontos(self, pontos=[]):
        self.__lista_pontos = pontos

    def set_matriz_perspectiva(self, fovy, aspect, z_near, z_far):
        """
        Gera a matriz de projeção do tipo perspectiva, segundo os parâmetros fornecidos
        :param fovy: ângulo de abertura(graus)
        :param aspect:
        :param z_near:
        :param z_far:
        :return: void
        """
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
        """
        Gera a matriz de projeção do tipo paralela, segundo os parâmetros fornecidos
        :param x_left:
        :param x_right:
        :param y_top:
        :param y_bottom:
        :param z_near:
        :param z_far:
        :return: void
        """
        self.__matriz_proj_paralela = np.matrix(
            [
                [2/(x_right-x_left), 0.0, 0.0, -((x_right+x_left)/(x_right-x_left))],
                [0.0, 2/(y_top-y_bottom), 0.0, -((y_top+y_bottom)/(y_top-y_bottom))],
                [0.0, 0.0, -(2/(z_far-z_near)), -((z_far+z_near)/(z_far-z_near))],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )

    def get_pontos_perspectiva(self):
        """
        Aplica a transformação perspectiva e retorna os pontos em R2
        :return: lista de pontos no formato: [[x1, y1], [x2, y2], ...]
        """
        perspectiva_2d = []
        for ponto in self.__lista_pontos:
            temp = self.__matriz_proj_perspec * ponto.get_matriz_coluna()
            ponto_2d = [round(temp.item(0, 0)/temp.item(3, 0), 2), round(temp.item(1, 0)/temp.item(3, 0), 2)]
            perspectiva_2d.append(ponto_2d)
        return perspectiva_2d

    def get_pontos_paralela(self):
        """
        Aplica a transformação paralela e retorna os pontos em R2
        :return: lista de pontos no formato: [[x1, y1], [x2, y2], ...]
        """
        paralela_2d = []
        for ponto in self.__lista_pontos:
            temp = self.__matriz_proj_paralela * ponto.get_matriz_coluna()
            ponto_2d = [round(temp.item(0, 0)/temp.item(3, 0), 2), round(temp.item(1, 0)/temp.item(3, 0), 2)]
            paralela_2d.append(ponto_2d)
        return paralela_2d