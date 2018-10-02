import csv
from src.Ponto import Ponto
from src.ObjetoDesenho import Objeto_Desenho


class Ler_Arquivo:

    def __init__(self, arquivo_pontos, arquivo_linhas):
        self.__arquivo_pontos = arquivo_pontos
        self.__arquivo_linhas = arquivo_linhas

    def ler_arquivo(self):
        conj_pontos = {}

        # Carregamento dos pontos
        with open(self.__arquivo_pontos, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = Ponto(float(row['x']), float(row['y']), float(row['z']))
                conj_pontos[row['label']] = obj

        # carregamento da ordem das linhas
        conj_linhas = {}
        with open(self.__arquivo_linhas, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                obj = (row['origem'], row['destino'])
                conj_linhas[row['label']] = obj

        ObjDesenho = Objeto_Desenho(conj_pontos, conj_linhas)
        return ObjDesenho
