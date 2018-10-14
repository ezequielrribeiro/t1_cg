import math as mth
from typing import List

import numpy as np

from src.modelo.Ponto import Ponto


class Transformacoes3:
    """
    Classe responsável por aplicar transformações em um conjunto de pontos
    (estes representam um objeto qualquer).
    Aplica transformações de translação, dimensão e rotação
    Sua ordem de execução:
    1 - adiciona_ponto (repetir até adicionar todos os pontos do objeto)
    2 - empilha_* ("empilhar" as transformações desejadas)
    3 - gera_matriz_transf (gerar a matriz final de transformação, que é a combinação de todas as
    transformações empilhadas anteriormente)
    4 - aplicar_transformacoes (aplica as transformacoes nos pontos)
    5 - get_pontos (obter os pontos modificados)

    Obs.: As instâncias dos objetos Ponto retornados pela classe são cópias dos objetos originais,
    não modificando as instâncias de entrada.
    """

    def __init__(self):
        self.__pontos = []
        self.__matrizes_transf = []
        self.__matriz_final = []

    def adiciona_ponto(self, ponto):
        """
        Adiciona uma cópia do ponto à lista de pontos interna
        :param ponto: objeto do tipo Ponto a ser adicionado
        :return: void
        """
        self.__pontos.append(ponto)

    def reset_transformacoes(self):
        """
        Coloca a classe de transformações na 'estaca zero' novamente,
        limpando a pilha de transformações e matrizes
        :return: void
        """
        self.__pontos = []
        self.__matrizes_transf = []
        self.__matriz_final = []


    def set_pontos(self, conjunto_pontos=[]):
        """
        Define o conjunto de pontos a serem aplicadas as transformações
        :param conjunto_pontos: lista
        :return: void
        """
        self.__pontos = conjunto_pontos


    def empilha_translacao(self, tr_x, tr_y, tr_z):
        """
        Move o objeto em k unidades
        :param tr_x: número de unidades a transladar em x
        :param tr_y: número de unidades a transladar em y
        :param tr_z: número de unidades a transladar em z
        :return: void
        """
        tr = np.matrix(
            [
                [1.0, 0.0, 0.0, tr_x],
                [0.0, 1.0, 0.0, tr_y],
                [0.0, 0.0, 1.0, tr_z],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        self.__matrizes_transf.append(tr)

    def empilha_escala(self, s_x, s_y, s_z):
        """
        Escalona o objeto em k unidades
        :param s_x: número de unidades a escalonar em x
        :param s_y: número de unidades a escalonar em y
        :param s_z: número de unidades a escalonar em z
        :return: void
        """
        es = np.matrix(
            [
                [s_x, 0.0, 0.0, 0.0],
                [0.0, s_y, 0.0, 0.0],
                [0.0, 0.0, s_z, 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        self.__matrizes_transf.append(es)

    def empilha_rotacao_x(self, angulo):
        """
        Rotacionar o objeto em k graus no eixo x
        :param angulo: ângulo (em graus) a rotacionar o objeto
        :return: void
        """
        ang_rad = mth.radians(angulo)
        rx = np.matrix(
            [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, mth.cos(ang_rad), (-1) * mth.sin(ang_rad), 0.0],
                [0.0, mth.sin(ang_rad), mth.cos(ang_rad), 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        self.__matrizes_transf.append(rx)

    def empilha_rotacao_y(self, angulo):
        """
        Rotacionar o objeto em k graus no eixo y
        :param angulo: ângulo (em graus) a rotacionar o objeto
        :return: void
        """
        ang_rad = mth.radians(angulo)
        ry = np.matrix(
            [
                [mth.cos(ang_rad), 0.0, mth.sin(ang_rad), 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [(-1) * mth.sin(ang_rad), 0.0, mth.cos(ang_rad), 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        self.__matrizes_transf.append(ry)

    def empilha_rotacao_z(self, angulo):
        """
        Rotacionar o objeto em k graus no eixo z
        :param angulo: ângulo (em graus) a rotacionar o objeto
        :return: void
        """
        ang_rad = mth.radians(angulo)
        rz = np.matrix(
            [
                [mth.cos(ang_rad), (-1) * mth.sin(ang_rad), 0.0, 0.0],
                [mth.sin(ang_rad), mth.cos(ang_rad), 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        self.__matrizes_transf.append(rz)

    def gera_matriz_transf(self):
        """
        Faz a combunação de todas as matrizes de transformação empilhadas
        anteriormente
        :return: void
        """
        m_t = np.matrix(
            [
                [1.0, 0.0, 0.0, 0.0],
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, 1.0, 0.0],
                [0.0, 0.0, 0.0, 1.0]
            ]
        )
        while self.__matrizes_transf:
            m_t = m_t * self.__matrizes_transf.pop()
        self.__matriz_final = m_t

    def aplicar_transformacoes(self):
        """
        Aplica as transformações combinadas sobre o objeto
        :return: void
        """
        result: List[Ponto] = []
        for ponto in self.__pontos:
            temp = self.__matriz_final * ponto.get_matriz_coluna()

            ponto.set_x(temp.item(0, 0))
            ponto.set_y(temp.item(1, 0))
            ponto.set_z(temp.item(2, 0))
            result.append(ponto)
        self.__pontos = result

    def get_pontos(self) -> List[Ponto]:
        """
        Retorna o objeto em formato de lista
        :return: lista do tipo Ponto
        """
        return self.__pontos
