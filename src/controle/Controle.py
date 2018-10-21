from src.modelo.LerArquivo import Carrega_Objeto_Desenho_Arquivo
from src.modelo.Transformacoes import Transformacoes3
from src.modelo.Camera import Camera
from src.modelo.Projecao import Projecao
from src.modelo.Viewport import Viewport
from src.modelo.ObjetoDesenho import Objeto_Desenho
import copy

class Controle:
    def __init__(self):
        self.__obj_desenho = None
        self.__parametros_padrao = None
        self.__obj_desenho_view = None
        self.reset_parametros()
        self.__objeto_transf = Transformacoes3()
        self.__camera_transf = Camera()
        self.__projecao = Projecao()
        self.__viewport = Viewport()

    def reset_parametros(self):
        self.__parametros_padrao = self.get_parametros_padrao()

    def get_parametros_padrao(self):
        return {
            'objeto': {
                'transl': [0.0, 0.0, 0.0],
                'escala': [1.0, 1.0, 1.0],
                'rotacao': [0.0, 60.0, 0.0]
            },
            'camera': {
                'posicao': [0.0, 0.0, 2.0],
                'rotacao': [0.0, 0.0, 0.0]
            },
            'projecao': {
                'definida': 'perspectiva',
                'perspectiva': {
                    'fovy': 67,
                    'aspect': 1,
                    'z_near': 0.1,
                    'z_far': 100
                },
                'paralela': {
                    'x_left': -1.0,
                    'x_right': 1.0,
                    'y_top': 1.0,
                    'y_bottom': -1.0,
                    'z_near': -1.0,
                    'z_far': 1.0
                }
            },
            'viewport': {
                'win_min': [-1, -1],
                'win_max': [1, 1],
                'vp_min': [0, 0],
                'vp_max': [400, 400]
            }
        }

    def carrega_arquivo(self, arquivo_pontos, arquivo_linhas):
        """
        Carregamento do arquivo (no formato .csv) para a memória
        :param arquivo_pontos: endereço do arquivo .csv contendo os pontos do objeto
        :param arquivo_linhas: endereço do arquivo .csv contendo as linhas do objeto
        :return: void
        """
        desenho_arquivo = Carrega_Objeto_Desenho_Arquivo()
        self.__obj_desenho = desenho_arquivo.carrega_objeto_arquivo(arquivo_pontos, arquivo_linhas)
        self.reset_parametros()

    def aplica_parametros(self, parametros):
        """
        Aplica as transformacoes sobre o objeto segundo os parametros
        :param parametros: dicionario contendo as informacoes para as modificacoes
        :return: void
        """
        # Transformações sobre o objeto no mundo
        self.__objeto_transf.reset_transformacoes()
        listaPontos = self.__obj_desenho.get_conj_pontos()

        for key in listaPontos:
            self.__objeto_transf.adiciona_ponto(copy.copy(listaPontos[key]))

        # Escalonar o objeto
        obj_esc = parametros['objeto']['escala']
        self.__objeto_transf.empilha_escala(obj_esc[0], obj_esc[1], obj_esc[2])

        # Rotacionar o objeto
        obj_rot = parametros['objeto']['rotacao']
        self.__objeto_transf.empilha_rotacao_x(obj_rot[0])
        self.__objeto_transf.empilha_rotacao_y(obj_rot[1])
        self.__objeto_transf.empilha_rotacao_z(obj_rot[2])

        # Transladar o objeto
        obj_transl = parametros['objeto']['transl']
        self.__objeto_transf.empilha_translacao(obj_transl[0], obj_transl[1], obj_transl[2])

        self.__objeto_transf.gera_matriz_transf()
        self.__objeto_transf.aplicar_transformacoes()

        # Câmera - setando pontos do objeto transformados
        self.__camera_transf.reset_camera()
        self.__camera_transf.set_conjunto_pontos(self.__objeto_transf.get_pontos())
        # Câmera - Translacao
        cam_t = parametros['camera']['posicao']
        self.__camera_transf.set_camera_pos(cam_t[0], cam_t[1], cam_t[2])
        # Câmera - rotação
        cam_rot = parametros['camera']['rotacao']
        self.__camera_transf.rotacionar_camera_x(cam_rot[0])
        self.__camera_transf.rotacionar_camera_y(cam_rot[1])
        self.__camera_transf.rotacionar_camera_z(cam_rot[2])
        self.__camera_transf.aplica_transformacoes_camera()

        # Projeção
        self.__projecao.set_lista_pontos(self.__camera_transf.obter_coordenadas_visualizacao())

        pontos_projecao = None
        if parametros['projecao']['definida'] == 'perspectiva':
            perspec = parametros['projecao']['perspectiva']
            self.__projecao.set_matriz_perspectiva(perspec['fovy'], perspec['aspect'], perspec['z_near'],
                                                   perspec['z_far'])
            pontos_projecao = self.__projecao.get_pontos_perspectiva()
        else:
            paralela = parametros['projecao']['paralela']
            self.__projecao.set_matriz_paralela(paralela['x_left'], paralela['x_right'], paralela['y_top'],
                                                paralela['y_bottom'], paralela['z_near'], paralela['z_far'])
            pontos_projecao = self.__projecao.get_pontos_paralela()

        # Viewport
        win_min = parametros['viewport']['win_min']
        win_max = parametros['viewport']['win_max']
        self.__viewport.set_window(win_min[0], win_min[1], win_max[0], win_max[1])
        self.__viewport.set_pontos(pontos_projecao)
        self.__viewport.transformar()

        # Lista transformada
        listaTemp = self.__viewport.get_coordenadas_dispositivo()
        listaTransform = {}
        i = 0
        for chave in listaPontos:
            listaTransform[chave] = listaTemp[i]
            i += 1

        # novo objeto para o desenho
        self.__obj_desenho_view = Objeto_Desenho(listaTransform, self.__obj_desenho.get_conj_vertices())

    def get_objeto_desenho(self) -> Objeto_Desenho:
        return self.__obj_desenho_view
