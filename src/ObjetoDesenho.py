class Objeto_Desenho:
    """
    Classe para manipulação dos pontos e ordem dos vértices a serem desenhados pela aplicação
    """
    def __init__(self, conj_pontos={}, conj_vertices=[]):
        """
        Inicialização da classe
        :param conj_pontos: dicionário do tipo: {'label_ponto_1':Ponto1, 'label_ponto_2':Ponto2, ...}
        :param conj_vertices: lista de listas contendo a ordem de 'ligação' dos pontos (para desenhar as linhas)
        """
        self.__conj_pontos = conj_pontos
        self.__conj_vertices = conj_vertices

    def get_conj_pontos(self):
        """
        Obter o dicionário dos pontos
        :return: dicionário do tipo: {'label_ponto_1':Ponto1, 'label_ponto_2':Ponto2, ...}
        """
        return self.__conj_pontos

    def get_conj_vertices(self):
        """
        Obter lista de vértices
        :return: list do tipo: [['label_ponto_origem1', 'label_ponto_destino1'],
        ['label_ponto_origem2', 'label_ponto_destino2'], ...]
        """
        return self.__conj_vertices

    def set_conj_pontos(self, conj_pontos={}):
        """
        Definir o conjunto de pontos a serem manipulados / plotados
        :param conj_pontos: dicionário do tipo: {'label_ponto_1':Ponto1, 'label_ponto_2':Ponto2, ...}
        :return: void
        """
        self.__conj_pontos = conj_pontos

    def set_conj_vertices(self, conj_vertices=[]):
        """
        Definir conjunto da ordem da ligação dos pontos
        :param conj_vertices: list do tipo: [['label_ponto_origem1', 'label_ponto_destino1'],
        ['label_ponto_origem2', 'label_ponto_destino2'], ...]
        :return: void
        """
        self.__conj_vertices = conj_vertices

