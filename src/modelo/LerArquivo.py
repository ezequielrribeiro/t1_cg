import csv
from src.modelo.Ponto import Ponto
from src.modelo.ObjetoDesenho import Objeto_Desenho


class Carrega_Objeto_Desenho_Arquivo:
    """
    Classe para ler um arquivo CSV e carregar para a memória um objeto do tipo
    ObjetoDesenho, para serem aplicadas as transformações e visualização
    """

    def __init__(self):
        """
        Inicialização da classe

        """
        pass

    def carrega_objeto_arquivo(self, arquivo_pontos='', arquivo_linhas='') -> Objeto_Desenho:
        """
        Método que lê os arquivos de texto e retorna uma instância objeto do tipo
        ObjetoDesenho na memória
        :param arquivo_pontos: arquivo CSV contendo as coordenadas X e Y dos pontos
        :param arquivo_linhas: arquivo CSV contendo a ordem de ligação dos pontos
        :return: objeto do tipo ObjetoDesenho, None em caso de falha
        """
        if arquivo_pontos == '' or arquivo_linhas == '':
            return None

        conj_pontos = {}

        # Carregamento dos pontos
        with open(arquivo_pontos, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Ponto(float(row['x']), float(row['y']), float(row['z']))
                conj_pontos[row['label']] = obj

        # carregamento da ordem das linhas
        conj_linhas = []
        with open(arquivo_linhas, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = [row['origem'], row['destino']]
                conj_linhas.append(obj)

        ObjDesenho = Objeto_Desenho(conj_pontos, conj_linhas)
        return ObjDesenho
