import Funciones as f
import Preguntas as p
from tkinter import *
from PIL import ImageTk, Image
import numpy as np

class Interfaz:
    def __init__(self) -> None:
        pass
    
    root = Tk ()
    root.title("BobExperto")
    root.resizable(False,False)
    root.geometry("647x540")
    root.iconbitmap("./img/00Bob.ico")
    imagen = ImageTk.PhotoImage(Image.open('./img/main.png'))
    label = Label(image=imagen)
    label.pack()
    
    def main ():
        p.Preguntas.preguntas("pantallaazul")

    btn = Button(
        root, text="Iniciar Diagnóstico",
        bg = "gray",
        fg = "purple",
        command=main,
        width=600).pack()
    root.mainloop()


