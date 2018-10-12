from src.LerArquivo import Ler_Arquivo
from src.Transformacoes import Transformacoes3
from src.Camera import Camera
from src.Projecao import Projecao
from src.Viewport import Viewport


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
projeta = Projecao(camera.obter_coordenadas_visualizacao())
projeta.set_matriz_perspectiva(67,1,0.1,100)
viewport = Viewport()
viewport.set_window(-1, -1, 1, 1)
viewport.set_pontos(projeta.get_pontos_perspectiva())
viewport.transformar()


for key in viewport.get_coordenadas_dispositivo():
    print(key)

#transforma.empilha_rotacao_x()

#print(ObjDesenho.__dict__)
