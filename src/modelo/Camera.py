from typing import List

from src.modelo.Transformacoes import Transformacoes3
from src.modelo.Ponto import Ponto


class Camera:
    """
    Classe responsável por aplicar as transformações de translação e rotação sobre o objeto,
    simulando uma câmera a observar o mesmo
    """

    def __init__(self, conjunto_pontos=[]):
        self.__conj_pontos = []
        for ponto in conjunto_pontos:
            self.__conj_pontos.append(ponto.get_copia())

        self.__transf_camera = Transformacoes3()
        self.set_conjunto_pontos(self.__conj_pontos)

    def reset_camera(self):
        """
        Põe a câmera no estado inicial, o mesmo de quando foi
        iniciada
        :return: void
        """
        self.__transf_camera.reset_transformacoes()
        self.set_conjunto_pontos(self.__conj_pontos)

    def set_conjunto_pontos(self, conjunto_pontos=[]):
        """
        Definir o conjunto de pontos a serem modificados
        :param conjunto_pontos:
        :return:
        """
        for ponto in conjunto_pontos:
            self.__transf_camera.adiciona_ponto(ponto.get_copia())

    def set_camera_pos(self, x, y, z):
        """
        Translada a câmera para um ponto no R3
        :param x: coordenada no eixo x para transladar a câmera
        :param y: coordenada no eixo y para transladar a câmera
        :param z: coordenada no eixo z para transladar a câmera
        :return: void
        """
        self.__transf_camera.empilha_translacao((-1)*x, (-1)*y, (-1)*z)

    def rotacionar_camera_x(self, angulo):
        """
        Empilha uma rotação de K graus (no eixo x) na câmera
        :param angulo: ângulo (em graus) que a câmera será rotacionada no eixo x
        :return: void
        """
        self.__transf_camera.empilha_rotacao_x(-angulo)

    def rotacionar_camera_y(self, angulo):
        """
        Empilha uma rotação de K graus (no eixo y) na câmera
        :param angulo: ângulo (em graus) que a câmera será rotacionada no eixo y
        :return: void
        """
        self.__transf_camera.empilha_rotacao_y(-angulo)

    def rotacionar_camera_z(self, angulo):
        """
        Empilha uma rotação de K graus (no eixo z) na câmera
        :param angulo: ângulo (em graus) que a câmera será rotacionada no eixo z
        :return: void
        """
        self.__transf_camera.empilha_rotacao_z(-angulo)

    def aplica_transformacoes_camera(self):
        """
        Aplica todas as transformações previamente empilhadas nos pontos do objeto
        :return: void
        """
        self.__transf_camera.gera_matriz_transf()
        self.__transf_camera.aplicar_transformacoes()

    def obter_coordenadas_visualizacao(self) -> List[Ponto]:
        """
        São obtidas as coordenadas do objeto modificadas pelas transformações aplicadas
        :return: lista do tipo Ponto(objeto)
        """
        return self.__transf_camera.get_pontos()
