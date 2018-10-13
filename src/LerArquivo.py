import csv
from src.Ponto import Ponto
from src.ObjetoDesenho import Objeto_Desenho


class Ler_Arquivo:
    """
    Classe para ler um arquivo CSV e carregar para a memória um objeto do tipo
    ObjetoDesenho, para serem aplicadas as transformações e visualização
    """

    def __init__(self, arquivo_pontos, arquivo_linhas):
        """
        Inicialização da classe
        :param arquivo_pontos: arquivo CSV contendo as coordenadas X e Y dos pontos
        :param arquivo_linhas: arquivo CSV contendo a ordem de ligação dos pontos
        """
        self.__arquivo_pontos = arquivo_pontos
        self.__arquivo_linhas = arquivo_linhas

    def ler_arquivo(self):
        """
        Método que lê os arquivos de texto e retorna uma instância objeto do tipo
        ObjetoDesenho na memória
        :return: objeto do tipo ObjetoDesenho
        """
        conj_pontos = {}

        # Carregamento dos pontos
        with open(self.__arquivo_pontos, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Ponto(float(row['x']), float(row['y']), float(row['z']))
                conj_pontos[row['label']] = obj

        # carregamento da ordem das linhas
        conj_linhas = []
        with open(self.__arquivo_linhas, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = [row['origem'], row['destino']]
                conj_linhas.append(obj)

        ObjDesenho = Objeto_Desenho(conj_pontos, conj_linhas)
        return ObjDesenho
