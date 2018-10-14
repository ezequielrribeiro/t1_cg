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
        self.__parametros = None
        self.__parametros = self.get_parametros_padrao()


    def get_parametros_padrao(self):
        return {
            'objeto': {
                'translacao': [0.0, 0.0, 0.0],
                'escala': [1.0, 1.0, 1.0],
                'rotacao': [0.0, 0.0, 0.0]
            },
            'camera': {
                'posicao': [0.0, 0.0, 0.0],
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

                }
            },
            'viewport': {
                'win_min': [-1,-1],
                'win_max': [1, 1],
                'vp_min': [0, 0],
                'vp_max': [400, 400]
            }
        }

    def carrega_arquivo(self, nome_arquivo):
        """
        Carregamento do arquivo (no formato .csv) para a memória
        :param nome_arquivo: primeiro nome do arquivo, sem .csv
        (formato do nome dos arquivos carregados: nome_arquivo_pontos.csv, nome_arquivo_linhas.csv)
        :return: void
        """
        objeto_desenho_arquivo = Carrega_Objeto_Desenho_Arquivo()
        self.__obj_desenho = objeto_desenho_arquivo.carrega_objeto_arquivo(nome_arquivo+"_pontos.csv",
                                                                           nome_arquivo+"_linhas.csv")

    def aplica_parametros(self, parametros):
        """
        Aplica os parametros sobre o objeto carregado em memoria
        :return: void
        """