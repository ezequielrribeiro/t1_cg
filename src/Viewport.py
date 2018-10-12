class Viewport:
    """
    Classe responsável por pelo passo final do mapeamento dos pontos do objeto para as coordenadas
    de uma viewport (coordenadas do dispositivo)
    """

    def __init__(self, vp_min_x=0, vp_min_y=0, vp_max_x=400, vp_max_y=400):
        """
        Inicialização da classe, podendo ser setados os valores mínimos e
        máximos para x e y da viewport
        :param vp_min_x: valor mínimo inteiro de x da viewport
        :param vp_min_y: valor mínimo inteiro de y da viewport
        :param vp_max_x: valor máximo inteiro de x da viewport
        :param vp_max_y: valor máximo inteiro de y da viewport
        """
        self.__window = None
        self.__pontos = None
        self.__viewport_min = [vp_min_x, vp_min_y]
        self.__viewport_max = [vp_max_x, vp_max_y]

    def set_window(self, wmin_x, wmin_y, wmax_x, wmax_y):
        """
        Setar as coordenadas mínimas e máximas de x e y da window
        :param wmin_x: menor coordenada x da window
        :param wmin_y: menor coordenada y da window
        :param wmax_x: maior coordenada x da window
        :param wmax_y: maior coordenada y da window
        :return: void
        """
        self.__window_min = [wmin_x, wmin_y]
        self.__window_max = [wmax_x, wmax_y]

    def set_pontos(self, lista_pontos):
        """
        Setar a lista de pontos a serem mapeados
        :param lista_pontos: pontos a mapear do tipo: [[x1, y1], [x2, y2], ...]
        :return: void
        """
        self.__pontos = lista_pontos

    def transformar(self):
        """
        Aplica o mapeamento na lista de pontos fornecida
        :return: void
        """
        coordenadas_dispositivo = []
        for ponto in self.__pontos:
            coordenadas_dispositivo.append(self.__get_viewport_coord__(ponto[0], ponto[1]))
            self.__pontos = coordenadas_dispositivo

    def __get_viewport_coord__(self, x_w, y_w):
        """
        Mapeia as coordenadas de um ponto na window para as coordenadas da viewport
        :param x_w: coordenada x do ponto a ser mapeado
        :param y_w: coordenada y do ponto a ser mapeado
        :return: [ponto_x_viewport, ponto_y_viewport]
        """
        vp_x = (((x_w - self.__window_min[0]) * (self.__viewport_max[0] - self.__viewport_min[0])) /
                (self.__window_max[0] - self.__window_min[0])) + self.__viewport_min[0]

        vp_y = (((y_w - self.__window_min[1]) * (self.__viewport_max[1] - self.__viewport_min[1])) /
                (self.__window_max[1] - self.__window_min[1])) + self.__viewport_min[1]
        return [vp_x, vp_y]

    def get_coordenadas_dispositivo(self):
        """
        Obter os pontos mapeados
        :return: lista de pontos do tipo list: [[x1,y1], [x2, y2], ...]
        """
        return self.__pontos
