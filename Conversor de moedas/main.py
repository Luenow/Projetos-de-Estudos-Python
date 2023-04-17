from tkinter import Tk, ttk
from tkinter import *

# importando bibliotecas externas -----------------------

from PIL import Image, ImageTk, ImageOps, ImageDraw



# cores --------------------------------- 
cor0 = "#FFFFFF"  # white / branca
cor1 = "#333333"  # black / preta
cor2 = "#38576b"  # dark blue / azul escuro

# configurando a janela -------------------

janela = Tk()
janela.geometry('300x320')
janela.title('Conversor')
janela.configure(bg=cor0)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Divisao da janela------

frame_cima = Frame(janela, width=300, height=60, padx=0, pady=0, bg=cor2, relief='flat')
frame_cima.grid(row=0,column=0, columnspan=2)


frame_baixo = Frame(janela, width=300, height=260, padx=0, pady=5, bg=cor0, relief='flat')
frame_baixo.grid(row=1,column=0, sticky=NSEW)


#  Configuracao frame acima -----








janela.mainloop()