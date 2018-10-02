from src.LerArquivo import Ler_Arquivo
from src.Transformacoes import Transformacoes3


leArquivo = Ler_Arquivo("../pontos.csv", "../desenha_linhas.csv")
ObjDesenho = leArquivo.ler_arquivo()
listaPontos = ObjDesenho.get_conj_pontos()
transforma = Transformacoes3()

for key in listaPontos:
    transforma.adiciona_ponto(listaPontos[key])

transforma.empilha_translacao(2,2,2)
transforma.gera_matriz_transf()
transforma.aplicar_transformacoes()
listanova = transforma.get_pontos()
for key in listanova:
    print(key.__dict__)

#transforma.empilha_rotacao_x()

#print(ObjDesenho.__dict__)
