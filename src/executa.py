from src.modelo.LerArquivo import Carrega_Objeto_Desenho_Arquivo
from src.modelo.Transformacoes import Transformacoes3
from src.modelo.Camera import Camera
from src.modelo.Projecao import Projecao
from src.modelo.Viewport import Viewport
from src.modelo.ObjetoDesenho import Objeto_Desenho
import copy
from src.controle.Controle import Controle
from tkinter import *


"""
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
"""
controle = Controle()
controle.carrega_arquivo("../pontos.csv", "../desenha_linhas.csv")
parametros = controle.get_parametros_padrao()
#controle.reset_parametros()
controle.aplica_parametros(parametros)
obj_view = controle.get_objeto_desenho()
print(obj_view.__dict__)
master = Tk()

canvas_width = 400
canvas_height = 400
w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()
lista_imprime = obj_view.get_conj_pontos()
for ponto in lista_imprime:
    print(ponto)
    w.create_text(lista_imprime[ponto][0], lista_imprime[ponto][1], fill="darkblue", font="Times 20 italic bold",
                        text=ponto)
    w.create_oval(lista_imprime[ponto][0], lista_imprime[ponto][1], lista_imprime[ponto][0], lista_imprime[ponto][1], width=0.01, fill="white")

linhas_imprimir = obj_view.get_conj_vertices()
for linha in linhas_imprimir:
    print(linha)
    w.create_line(lista_imprime[linha[0]][0], lista_imprime[linha[0]][1], lista_imprime[linha[1]][0], lista_imprime[linha[1]][1], fill="white")
mainloop()


#transforma.empilha_rotacao_x()

#print(novoDesenha.__dict__)
