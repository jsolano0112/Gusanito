import turtle
import time
from Jugador import *

#llamando clase jugador

cuerpoGusanito = []
nivelmax = 0
jugadores = []
#archivo
puntajeAlc = []
#archivo

ventana = turtle.Screen()
ventana.title("Juego de gusanito By Juana")
ventana.bgcolor("black")
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

#Barrera
barrera = turtle.Turtle()
barrera.goto(-220, 160)
barrera.pensize(2)
barrera.pencolor('white')
barrera.speed(2)
barrera.goto(220, 160)
barrera.hideturtle()



class Gusano:

    def mov(self):
        if cabeza.direction == "up":
            y = cabeza.ycor()  # almacenar coordenada en y
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

    def arriba(self):
        # para que el gusano de dirija a x direccion
        if cabeza.direction != "down":
            cabeza.direction = "up"

    def abajo(self):
        if cabeza.direction != "up":
            cabeza.direction = "down"

    def izquierda(self):
        if cabeza.direction != "right":
            cabeza.direction = "left"

    def derecha(self):
        if cabeza.direction != "left":
            cabeza.direction = "right"

    def obtenerPuntaje(self,nombre, nivelmax):
        #Es para obtener el puntaje max por cada que empiece a jugar nuevamente, sin cerrar la ventana
        try:
            archivo = open('PuntajeAltoDelJugador.txt', 'w')
            jugadores.append(nombre)
            puntajeAlc.append(nivelmax)

            for valorj,valorp in zip(jugadores, puntajeAlc):
                archivo.write(f'{valorj}: {valorp}\n')

        except Exception as e:
            print('se guardó el archivo')
        finally:
            archivo.close()

    def reiniciarJuego(self):
        time.sleep(1)
        cabeza.goto(0, 0)
        cabeza.direction = "stop"

        # Eliminar las partes de cuerpo
        for partes in cuerpoGusanito:
            partes.goto(1000, 1000)
        cuerpoGusanito.clear()





