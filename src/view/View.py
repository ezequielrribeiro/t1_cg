from tkinter import *
from src.modelo.ObjetoDesenho import Objeto_Desenho
from src.controle.Controle import Controle


class View:
    def __init__(self, master=None):
        self.__controle = Controle()
        self.__controle.carrega_arquivo("../../pontos.csv", "../../desenha_linhas.csv")
        self.__parametros = self.__controle.get_parametros_padrao()
        self.__controle.aplica_parametros(self.__parametros)
        self.__containers = []
        self.__controles_objeto = []
        self.__controles_camera = []
        self.__controles_wpvp = []
        self.__canvas = None
        for i in range(0, 4):
            self.__containers.append(self.__criar_container(master))
        for i in range(0, 9):
            self.__controles_objeto.append(self.__criar_spinbox(self.__containers[0], -100, 100, '%.1f', 0.1))
        for i in range(0, 6):
            self.__controles_camera.append(self.__criar_spinbox(self.__containers[1], -100, 100, '%.1f', 0.1))
        for i in range(0, 12):
            self.__controles_wpvp.append(self.__criar_spinbox(self.__containers[2], -200, 100, '%.1f', 0.1))

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

    def sx_objeto(self, event):
        valor_controle = float(self.__controles_objeto[3].get())
        self.__parametros['objeto']['escala'][0] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def sy_objeto(self, event):
        valor_controle = float(self.__controles_objeto[4].get())
        self.__parametros['objeto']['escala'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def sz_objeto(self, event):
        valor_controle = float(self.__controles_objeto[5].get())
        self.__parametros['objeto']['escala'][2] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def rx_objeto(self, event):
        valor_controle = float(self.__controles_objeto[6].get())
        self.__parametros['objeto']['rotacao'][0] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def ry_objeto(self, event):
        valor_controle = float(self.__controles_objeto[7].get())
        self.__parametros['objeto']['rotacao'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def rz_objeto(self, event):
        valor_controle = float(self.__controles_objeto[8].get())
        self.__parametros['objeto']['rotacao'][2] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def tx_camera(self, event):
        valor_controle = float(self.__controles_camera[0].get())
        self.__parametros['camera']['posicao'][0] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def ty_camera(self, event):
        valor_controle = float(self.__controles_camera[1].get())
        self.__parametros['camera']['posicao'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def tz_camera(self, event):
        valor_controle = float(self.__controles_camera[2].get())
        self.__parametros['camera']['posicao'][2] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def rx_camera(self, event):
        valor_controle = float(self.__controles_camera[3].get())
        self.__parametros['camera']['rotacao'][0] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def ry_camera(self, event):
        valor_controle = float(self.__controles_camera[4].get())
        self.__parametros['camera']['rotacao'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def rz_camera(self, event):
        valor_controle = float(self.__controles_camera[5].get())
        self.__parametros['camera']['rotacao'][2] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_winmin(self, event):
        valor_controle = float(self.__controles_wpvp[0].get())
        self.__parametros['viewport']['win_min'][0] = valor_controle
        self.__parametros['viewport']['win_min'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_winmax(self, event):
        valor_controle = float(self.__controles_wpvp[1].get())
        self.__parametros['viewport']['win_max'][0] = valor_controle
        self.__parametros['viewport']['win_max'][1] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_fovy(self, event):
        valor_controle = float(self.__controles_wpvp[2].get())
        self.__parametros['projecao']['definida'] = 'perspectiva'
        self.__parametros['projecao']['perspectiva']['fovy'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_znear(self, event):
        valor_controle = float(self.__controles_wpvp[3].get())
        self.__parametros['projecao']['definida'] = 'perspectiva'
        self.__parametros['projecao']['perspectiva']['z_near'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_zfar(self, event):
        valor_controle = float(self.__controles_wpvp[4].get())
        self.__parametros['projecao']['definida'] = 'perspectiva'
        self.__parametros['projecao']['perspectiva']['z_far'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_aspect(self, event):
        valor_controle = float(self.__controles_wpvp[5].get())
        self.__parametros['projecao']['definida'] = 'perspectiva'
        self.__parametros['projecao']['perspectiva']['aspect'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_xleft(self, event):
        valor_controle = float(self.__controles_wpvp[6].get())
        self.__parametros['projecao']['definida'] = 'paralela'
        self.__parametros['projecao']['paralela']['x_left'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_xright(self, event):
        valor_controle = float(self.__controles_wpvp[7].get())
        self.__parametros['projecao']['definida'] = 'paralela'
        self.__parametros['projecao']['paralela']['x_right'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_ybottom(self, event):
        valor_controle = float(self.__controles_wpvp[8].get())
        self.__parametros['projecao']['definida'] = 'paralela'
        self.__parametros['projecao']['paralela']['y_bottom'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_ytop(self, event):
        valor_controle = float(self.__controles_wpvp[9].get())
        self.__parametros['projecao']['definida'] = 'paralela'
        self.__parametros['projecao']['paralela']['y_top'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_pznear(self, event):
        valor_controle = float(self.__controles_wpvp[10].get())
        self.__parametros['projecao']['definida'] = 'paralela'
        self.__parametros['projecao']['paralela']['z_near'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())

    def set_pzfar(self, event):
        valor_controle = float(self.__controles_wpvp[11].get())
        self.__parametros['projecao']['definida'] = 'paralela'
        self.__parametros['projecao']['paralela']['z_far'] = valor_controle
        self.__controle.aplica_parametros(self.__parametros)
        self.desenha_canvas(self.__controle.get_objeto_desenho())


    def __definir_acoes_controles(self):
        self.__controles_objeto[0].bind("<Button-1>", self.tx_objeto)
        self.__controles_objeto[1].bind("<Button-1>", self.ty_objeto)
        self.__controles_objeto[2].bind("<Button-1>", self.tz_objeto)
        self.__controles_objeto[3].bind("<Button-1>", self.sx_objeto)
        self.__controles_objeto[4].bind("<Button-1>", self.sy_objeto)
        self.__controles_objeto[5].bind("<Button-1>", self.sz_objeto)
        self.__controles_objeto[6].bind("<Button-1>", self.rx_objeto)
        self.__controles_objeto[7].bind("<Button-1>", self.ry_objeto)
        self.__controles_objeto[8].bind("<Button-1>", self.rz_objeto)

        self.__controles_camera[0].bind("<Button-1>", self.tx_camera)
        self.__controles_camera[1].bind("<Button-1>", self.ty_camera)
        self.__controles_camera[2].bind("<Button-1>", self.tz_camera)
        self.__controles_camera[3].bind("<Button-1>", self.rx_camera)
        self.__controles_camera[4].bind("<Button-1>", self.ry_camera)
        self.__controles_camera[5].bind("<Button-1>", self.rz_camera)

        self.__controles_wpvp[0].bind("<Button-1>", self.set_winmin)
        self.__controles_wpvp[1].bind("<Button-1>", self.set_winmax)
        self.__controles_wpvp[2].bind("<Button-1>", self.set_fovy)
        self.__controles_wpvp[3].bind("<Button-1>", self.set_znear)
        self.__controles_wpvp[4].bind("<Button-1>", self.set_zfar)
        self.__controles_wpvp[5].bind("<Button-1>", self.set_aspect)

        self.__controles_wpvp[6].bind("<Button-1>", self.set_xleft)
        self.__controles_wpvp[7].bind("<Button-1>", self.set_xright)
        self.__controles_wpvp[8].bind("<Button-1>", self.set_ybottom)
        self.__controles_wpvp[9].bind("<Button-1>", self.set_ytop)
        self.__controles_wpvp[10].bind("<Button-1>", self.set_pznear)
        self.__controles_wpvp[11].bind("<Button-1>", self.set_pzfar)

    def __criar_container(self, master):
        container_temp = Frame(master)
        container_temp["width"] = 200
        container_temp["height"] = 400
        container_temp.pack(side=LEFT)
        return container_temp

    def __criar_spinbox(self, master, from_, to_, formato, incremento=1.0):
        w = Spinbox(master, from_=from_, to=to_)
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
        for ponto in lista_imprime:
            #print(ponto)
            w_canvas.create_text(lista_imprime[ponto][0], lista_imprime[ponto][1], fill="darkblue", font="Times 20 italic bold",
                                text=ponto)
            w_canvas.create_oval(lista_imprime[ponto][0], lista_imprime[ponto][1], lista_imprime[ponto][0], lista_imprime[ponto][1], width=0.01, fill="white")



root = Tk()
View(root)
root.mainloop()
