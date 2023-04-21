"""Juana Solano E."""
import sys
import turtle
import time
import random
import tkinter as tk
from tkinter import ttk, messagebox

posponer = 0.1
cuerpoGusanito = []
puntos = 0
nivelmax = 0
coloresCuerpo = ["red", "yellow", "blue", "pink", "purple"]



def eventoParaIniciar():
    if nombreJugador.get() == "":
        mensajeError = 'No has ingresado tu nombre.'
        messagebox.showerror('Falta entrada de datos', mensajeError)
        print("vacío")
    else:
        print("Se quitó la ventana")
        ventanatk.withdraw()


def nombreDelJugador():
    return nombreJugador.get()

def reiniciarJuego():
    time.sleep(1)
    cabeza.goto(0, 0)
    cabeza.direction = "stop"

    # Eliminar las partes de cuerpo
    for partes in cuerpoGusanito:
        partes.goto(1000, 1000)

    cuerpoGusanito.clear()
def mov():
    if cabeza.direction == "up":
            y = cabeza.ycor() #almacenar coordenada en y
            cabeza.sety(y + 20)

    if cabeza.direction == "down":
            y = cabeza.ycor()  # coordenada en y
            cabeza.sety(y - 20)

    if cabeza.direction == "left":
            x = cabeza.xcor()  # coordenada en x
            cabeza.setx(x - 20)

    if cabeza.direction == "right":
            x = cabeza.xcor()  # coordenada en x
            cabeza.setx(x + 20)
def arriba():
     # para que el gusano de dirija a x direccion
    if cabeza.direction != "down":
            cabeza.direction = "up"
def abajo():
    if cabeza.direction != "up":
        cabeza.direction = "down"
def izquierda():
    if cabeza.direction != "right":
        cabeza.direction = "left"
def derecha():
    if cabeza.direction != "left":
     cabeza.direction = "right"


#Ventana TKinter
ventanatk = tk.Tk()
ventanatk.geometry("300x100")
ventanatk.title('Jueguito del gusanito🐛')
ventanatk.resizable(0,0)

#para centrar
altura = ventanatk.winfo_reqheight()
anchura = ventanatk.winfo_reqwidth()
altura_pantalla = ventanatk.winfo_screenheight()
anchura_pantalla = ventanatk.winfo_screenwidth()
print(
    f"Altura: {altura}\nAnchura: {anchura}\nAltura de pantalla: {altura_pantalla}\nAnchura de pantalla: {anchura_pantalla}")
x = (anchura_pantalla // 2) - (anchura // 2)
y = (altura_pantalla // 2) - (altura // 2)

ventanatk.geometry(f"+{x}+{y}")

#Labels
bienvenido = tk.Label(ventanatk, text='Bienvenido')
bienvenido.pack()

pregunta = tk.Label(ventanatk, text='Ingresa tu nombre')
pregunta.pack()

#Textbox para recibir nombre del jugador
nombreJugador = ttk.Entry(ventanatk, width=20)
nombreJugador.pack()

#Botonsito para seguir
botonInicio = ttk.Button(ventanatk, text='Iniciar Juego😊', command=eventoParaIniciar)
botonInicio.pack()


#Ventana Turtle
#crear ventana


ventana = turtle.Screen()
ventana.title("Juego de gusanito By Juana")
ventana.bgcolor("#397441")
ventana.setup(width = 440, height = 440)
ventana.tracer(0) #para que se ejecute en la mitad


#Cabeza de gusanito
cabeza = turtle.Turtle()
cabeza.speed(0) #velocidad
cabeza.shape("square") #forma
cabeza.color("brown2")
cabeza.penup() #para no dejar rastro cuando se mueva
cabeza.goto(0, 0) #posicion
cabeza.direction = "stop"

#Comida
comida = turtle.Turtle()
comida.speed(0) #velocidad
comida.shape("circle") #forma
comida.color("red")
comida.penup() #para no dejar rastro


#Puntos
texto = turtle.Turtle()
texto.speed(0)
texto.color("Black")
texto.hideturtle()
texto.goto(0, 180)
texto.penup()
texto.fillcolor("red")
texto.write(f'Hola {nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center", font=("impact), 12"))

#Barrera
barrera = turtle.Turtle()
barrera.goto(-220, 160)
barrera.pensize(3) #grosor
barrera.color("black")
barrera.speed(2)
barrera.goto(220, 160)
barrera.hideturtle()


# conectar con el Teclado

ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

#Bucle para inicializar

while True:
        ventana.update()

        #si el gusanito está yendo para lado y+ que no esté disponible el y-
        if cabeza.direction == "up":
            if ventana.onkeypress(abajo, "Down"):
                cabeza.sety(y + 20)

        #si el gusanito toca los limites
        if cabeza.xcor() > 205 or cabeza.xcor() < -205 or cabeza.ycor() > 140 or cabeza.ycor() < -205:
          reiniciarJuego()
          puntos = 0
          texto.clear()
          texto.write(f'Hola {nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center",
                    font=("impact), 12"))

        #si el gusanito toca el propio cuerpo
        for partes in cuerpoGusanito:
            if partes.distance(cabeza) < 10:
                reiniciarJuego()
                puntos = 0
                texto.clear()
                texto.write(f'Hola {nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}',
                            align="center", font=("impact), 12"))

        #si el gusanito toca la comida
        if cabeza.distance(comida) < 20:
            x=random.randint(-10,10)*20 #numeros random para que se ubique la comida
            y=random.randint(-10,7)*20
            comida.goto(x,y)
            pass

            # partes de cuerpo
            partes = turtle.Turtle()
            partes.speed(0)  # velocidad
            partes.shape("square")  # forma
            if len(cuerpoGusanito) % 2 != 0:
                partes.color("black")
            else:
                partes.color(random.choice(coloresCuerpo))
            partes.penup()  # para no dejar rastro cuando se mueva
            # para que el ultimo segmento del cuerpo siga al de adelante
            cuerpoGusanito.append(partes)

            puntos += 1
            if puntos > nivelmax:
                nivelmax = puntos


            texto.clear()
            texto.write(f'Hola {nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center",
                        font=("impact), 12"))

        #mover cuerpo de la serpiente
        totalPartes = len(cuerpoGusanito)
        # len devuelve la logitud de la lista
        #este ciclo permite que al avanzar el gusano, sus partes se posicionen en las antecesoras
        for i in range(totalPartes -1, 0, -1):
            x = cuerpoGusanito[i-1].xcor()
            y = cuerpoGusanito[i-1].ycor()
            cuerpoGusanito[i].goto(x,y)

        if totalPartes > 0:
            x = cabeza.xcor()
            y = cabeza.ycor()
            cuerpoGusanito[0].color("blue")
            #para que el primer elemento se pegue a la cabeza
            cuerpoGusanito[0].goto(x,y)

        mov()
        time.sleep(posponer)





ventanatk.mainloop()