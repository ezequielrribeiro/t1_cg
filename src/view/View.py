from tkinter import *
from src.modelo.ObjetoDesenho import Objeto_Desenho
from src.controle.Controle import Controle
import copy


class View:
    def __init__(self, master=None):
        self.__controle = Controle()
        self.__controle.carrega_arquivo("../../pontos.csv", "../../desenha_linhas.csv")
        self.__parametros = self.__controle.get_parametros_padrao()
        self.__controle.aplica_parametros(self.__parametros)
        self.__containers = []
        self.__controles_objeto = []
        self.__canvas = None
        for i in range(0, 4):
            self.__containers.append(self.__criar_container(master))
        for i in range(0, 9):
            self.__controles_objeto.append(self.__criar_spinbox(self.__containers[0], -10, 10, '%.1f', 0.1))

        # Widget Canvas
        self.__containers[3]['width'] = 400
        self.__carrega_canvas(self.__containers[3])
        self.desenha_canvas(self.__controle.get_objeto_desenho())

        # Definir ações dos controles
        self.__definir_acoes_controles()


    def tx_objeto(self, event):
        valor_controle = float(self.__controles_objeto[0].get())
        self.__parametros['objeto']['transl'][0] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def ty_objeto(self, event):
        valor_controle = float(self.__controles_objeto[1].get())
        self.__parametros['objeto']['transl'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def tz_objeto(self, event):
        valor_controle = float(self.__controles_objeto[2].get())
        self.__parametros['objeto']['transl'][2] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def __definir_acoes_controles(self):
        self.__controles_objeto[0].bind("<Button-1>", self.tx_objeto)
        self.__controles_objeto[1].bind("<Button-1>", self.ty_objeto)
        self.__controles_objeto[2].bind("<Button-1>", self.tz_objeto)

    def __criar_container(self, master):
        container_temp = Frame(master)
        container_temp["width"] = 200
        container_temp["height"] = 400
        container_temp.pack(side=LEFT)
        return container_temp

    def __criar_spinbox(self, master, from_, to_, formato, incremento=1.0):
        w = Spinbox(master, from_=from_, to=to_, format=formato, increment=incremento)
        w.pack()
        return w

    def __carrega_canvas(self, master):
        canvas_width = 400
        canvas_height = 400
        self.__canvas = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        self.__canvas.pack()

    def desenha_canvas(self, objeto_desenho: Objeto_Desenho):
        w_canvas = self.__canvas
        # "limpar" a tela
        w_canvas.delete("all")
        # redesenhar o objeto
        self.__desenha_objeto(objeto_desenho)
        # atualizar canvas
        w_canvas.update()

    def __desenha_objeto(self, objeto_desenho: Objeto_Desenho):
        w_canvas = self.__canvas
        lista_imprime = objeto_desenho.get_conj_pontos()
        linhas_imprimir = objeto_desenho.get_conj_vertices()
        for linha in linhas_imprimir:
            w_canvas.create_line(lista_imprime[linha[0]][0], lista_imprime[linha[0]][1], lista_imprime[linha[1]][0],
                                 lista_imprime[linha[1]][1], fill="white")


root = Tk()
View(root)
root.mainloop()
