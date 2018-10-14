from src.modelo.LerArquivo import Carrega_Objeto_Desenho_Arquivo
from src.modelo.Transformacoes import Transformacoes3
from src.modelo.Camera import Camera
from src.modelo.Projecao import Projecao
from src.modelo.Viewport import Viewport
from src.modelo.ObjetoDesenho import Objeto_Desenho
import copy
from tkinter import *



leArquivo = Carrega_Objeto_Desenho_Arquivo()
ObjDesenho = leArquivo.carrega_objeto_arquivo("../pontos.csv", "../desenha_linhas.csv")
listaPontos = ObjDesenho.get_conj_pontos()
transforma = Transformacoes3()

for key in listaPontos:
    transforma.adiciona_ponto(copy.copy(listaPontos[key]))

transforma.empilha_rotacao_y(60)
transforma.gera_matriz_transf()
transforma.aplicar_transformacoes()
listanova = transforma.get_pontos()
camera = Camera(listanova)
camera.set_camera_pos(0, 0, 2)
camera.aplica_transformacoes_camera()
projeta = Projecao(camera.obter_coordenadas_visualizacao())
projeta.set_matriz_perspectiva(67, 1, 0.1, 100)
viewport = Viewport()
viewport.set_window(-1, -1, 1, 1)
viewport.set_pontos(projeta.get_pontos_perspectiva())
viewport.transformar()

# Lista transformada
listaTemp = viewport.get_coordenadas_dispositivo()
listaTransform = {}
i = 0
for chave in listaPontos:
    listaTransform[chave] = listaTemp[i]
    i+=1

# novo objeto para o desenho
novoDesenha = Objeto_Desenho(listaTransform, ObjDesenho.get_conj_vertices())

# nova lista de pontos (processados)

master = Tk()

canvas_width = 400
canvas_height = 400
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

for ponto in viewport.get_coordenadas_dispositivo():
    print(ponto)
    w.create_oval(ponto[0], ponto[1], ponto[0], ponto[1], width=0.01, fill="white")


mainloop()


#transforma.empilha_rotacao_x()

print(novoDesenha.__dict__)
