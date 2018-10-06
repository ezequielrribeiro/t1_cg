from src.LerArquivo import Ler_Arquivo
from src.Transformacoes import Transformacoes3
from src.Camera import Camera


leArquivo = Ler_Arquivo("../pontos.csv", "../desenha_linhas.csv")
ObjDesenho = leArquivo.ler_arquivo()
listaPontos = ObjDesenho.get_conj_pontos()
transforma = Transformacoes3()

for key in listaPontos:
    transforma.adiciona_ponto(listaPontos[key])

transforma.empilha_rotacao_y(60)
transforma.gera_matriz_transf()
transforma.aplicar_transformacoes()
listanova = transforma.get_pontos()
camera = Camera(listanova)
#camera.rotacionar_camera_x(20)
camera.set_camera_pos(0,0,2)
camera.aplica_transformacoes_camera()

for key in camera.obter_coordenadas_visualizacao():
    print(key.__dict__)

#transforma.empilha_rotacao_x()

#print(ObjDesenho.__dict__)
