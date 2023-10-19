import tkinter as tk # 'as' es una tiqueta donde nombra tkinter como tk y tkinter es para monstra los entorno grafico


# Importar los modulos restante de  tkinter

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FormularioClientes:
    
    def Formulario():
        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")
            base.mainloop()
            
        except ValueError as error:
            print("error al mostrar la interfaz, error: {}".format(error))
    
    Formulario()