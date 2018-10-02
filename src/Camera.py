from typing import List

from src.Transformacoes import Transformacoes3
from src.Ponto import Ponto


class Camera:

    def __init__(self, conjunto_pontos=[]):
        self.__transf_camera = Transformacoes3()
        for ponto in conjunto_pontos:
            self.__transf_camera.adiciona_ponto(ponto)

    def set_camera_pos(self, x, y, z):
        self.__transf_camera.empilha_translacao(-x, -y, -z)

    def rotacionar_camera_x(self, angulo):
        self.__transf_camera.empilha_rotacao_x(-angulo)

    def rotacionar_camera_y(self, angulo):
        self.__transf_camera.empilha_rotacao_y(-angulo)

    def rotacionar_camera_z(self, angulo):
        self.__transf_camera.empilha_rotacao_z(-angulo)

    def aplica_transformacoes_camera(self):
        self.__transf_camera.gera_matriz_transf()
        self.__transf_camera.aplicar_transformacoes()

    def obter_coordenadas_visualizacao(self) -> List[Ponto]:
        return self.__transf_camera.get_pontos()
