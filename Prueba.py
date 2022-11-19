import tkinter
from tkinter import *
from tkinter import ttk
raiz=Tk()
raiz.geometry('300x200')
raiz.title("Pokedex")
ttk.Button(raiz, text='Salir', command=quit).pack(side=BOTTOM)
raiz.mainloop()
