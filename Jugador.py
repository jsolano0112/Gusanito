import tkinter as tk
from tkinter import ttk, messagebox
from Gusano import *



#Ventana TKinter
ventanatk = tk.Tk()
ventanatk.title('Jueguito del gusanito🐛')
#para centrar
ancho_ventana = 300
alto_ventana = 100
x_ventana = ventanatk.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventanatk.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventanatk.geometry(posicion)


#Labels
bienvenido = tk.Label(ventanatk, text='Bienvenido')
bienvenido.pack()

pregunta = tk.Label(ventanatk, text='Ingresa tu nombre')
pregunta.pack()

#Textbox para recibir nombre del jugador
nombreJugador = ttk.Entry(ventanatk, width=20)
nombreJugador.pack()
class Jugador:
    def eventoParaIniciar(self):
        if nombreJugador.get() == "":
            mensajeError = 'No has ingresado tu nombre.'
            messagebox.showerror('Falta entrada de datos', mensajeError)
            print("vacío")
        else:
            print("Se quitó la ventana")
            ventanatk.withdraw()

    def nombreDelJugador(self):
        return nombreJugador.get()





