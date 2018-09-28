class Objeto_Desenho:
    def __init__(self, conj_pontos={}, conj_vertices={}):
        self.__conj_pontos = conj_pontos
        self.__conj_vertices = conj_vertices

    def get_conj_pontos(self):
        return self.__conj_pontos

    def get_conj_vertices(self):
        return self.__conj_vertices

    def set_conj_pontos(self, conj_pontos):
        self.__conj_pontos = conj_pontos

    def set_conj_vertices(self, conj_vertices):
        self.__conj_vertices = conj_vertices

