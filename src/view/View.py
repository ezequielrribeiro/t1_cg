from tkinter import *


class View:
    def __init__(self, master=None):
        self.__containers = []
        self.__controles_objeto = []
        for i in range(0, 4):
            self.__containers.append(self.__criar_container(master))
        for i in range(0, 9):
            self.__controles_objeto.append(self.__criar_spinbox(self.__containers[0], -10, 10, '%.1f', 0.1))

        # Widget Canvas
        self.__containers[3]['width'] = 400
        self.__carrega_canvas(self.__containers[3])


        """self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.pack()"""

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
        w = Canvas(master,
                   width=canvas_width,
                   height=canvas_height)
        w.pack()


root = Tk()
View(root)
root.mainloop()
