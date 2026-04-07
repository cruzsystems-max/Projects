import tkinter as tk
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt



root = Tk()
root.resizable(0, 0)
root.title("Algoritmo de planificación")
var_num = StringVar()








root.resizable(0, 0)
root.config(background="#32cb00")
# self.geometry("500x320+100+100")

def Clear():
    res = float(var_num.get())
    Com1.config(text="Hola")



frame = Frame(root, background="#1de9b6")
frame.pack(padx=10, pady=10, side=tk.LEFT, anchor=tk.N)
# se crean las tablas en base a entries y labels

lblName = Label(frame, text="Nombre del\nproceso").grid(row=0, column=1)
ent1F1 = Entry(frame, width=15, textvariable=var_num).grid(row=1, column=1)
ent1F2 = Entry(frame, width=15).grid(row=2, column=1)
ent1F3 = Entry(frame, width=15).grid(row=3, column=1)
ent1F4 = Entry(frame, width=15).grid(row=4, column=1)

lblBurst = Label(frame, text="Tiempo de\n CPU").grid(row=0, column=2)
ent2F1 = Entry(frame, width=15).grid(row=1, column=2)
ent2F2 = Entry(frame, width=15).grid(row=2, column=2)
ent2F3 = Entry(frame, width=15).grid(row=3, column=2)
ent2F4 = Entry(frame, width=15).grid(row=4, column=2)

lblArrive = Label(frame, text="Tiempo de\nLlegada").grid(row=0, column=3)
ent3F1 = Entry(frame, width=15).grid(row=1, column=3)
ent3F2 = Entry(frame, width=15).grid(row=2, column=3)
ent3F3 = Entry(frame, width=15).grid(row=3, column=3)
ent3F4 = Entry(frame, width=15).grid(row=4, column=3)

lblPriori = Label(frame, text="Prioridad \nde Proceso").grid(row=0, column=4)
ent4F1 = Entry(frame, width=15).grid(row=1, column=4)
ent4F2 = Entry(frame, width=15).grid(row=2, column=4)
ent4F3 = Entry(frame, width=15).grid(row=3, column=4)
ent4F4 = Entry(frame, width=15).grid(row=4, column=4)

lblPriori = Label(frame, text="Tiempo de\nEspera").grid(row=0, column=5)
Wait1 = Label(frame, background="#00e676", width=10).grid(row=1, column=5)
Wait2 = Label(frame, background="#00e676", width=10).grid(row=2, column=5)
Wait3 = Label(frame, background="#00e676", width=10).grid(row=3, column=5)
Wait4 = Label(frame, background="#00e676", width=10).grid(row=4, column=5)

lblPriori = Label(frame, text="Tiempo\nCompleto").grid(row=0, column=6)
Com1 = Label(frame, text="", background="#64dd17", width=10).grid(padx=3, pady=3, row=1, column=6)
Com2 = Label(frame, background="#64dd17", width=10).grid(padx=3, pady=3, row=2, column=6)
Com3 = Label(frame, background="#64dd17", width=10).grid(padx=3, pady=3, row=3, column=6)
Com4 = Label(frame, background="#64dd17", width=10).grid(padx=3, pady=3, row=4, column=6)

# se crea el boton que me permite calcular el resultado

Calcular = Button(frame, text="CALCULAR", command=lambda: Clear()).grid(padx=10, pady=20, row=5, column=1,columnspan=2, )




root.mainloop()