import random
from Gusano import *
from Jugador import *

puntos = 0
nivelmax = 0
posponer = 0.1
coloresCuerpo = ("red", "blue", "pink", "purple")

#llamando clase Gusano para utilizar metodos
metodo = Gusano()

#llamando clase jugador
metodosJugador = Jugador()

# conectar con el Teclado
ventana.listen()
ventana.onkeypress(metodo.arriba, "Up")
ventana.onkeypress(metodo.abajo, "Down")
ventana.onkeypress(metodo.izquierda, "Left")
ventana.onkeypress(metodo.derecha, "Right")


#Puntos
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.hideturtle()
texto.goto(0, 180)
texto.penup()
texto.fillcolor("red")
texto.write(f'Hola {metodosJugador.nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center", font=("impact, 12"))


#Botonsito para seguir
botonInicio = ttk.Button(ventanatk, text='Iniciar Juego😊', command=metodosJugador.eventoParaIniciar)
botonInicio.pack()



#Para inicializar

while True:
        ventana.update()

        #si el gusanito toca los limites
        if cabeza.xcor() > 205 or cabeza.xcor() < -205 or cabeza.ycor() > 140 or cabeza.ycor() < -205:
          metodo.obtenerPuntaje(metodosJugador.nombreDelJugador(),nivelmax)
          metodo.reiniciarJuego()
          puntos = 0
          texto.clear()
          texto.write(f'Hola {metodosJugador.nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center", font=("impact, 12"))

        #si el gusanito toca el propio cuerpo
        for partes in cuerpoGusanito:
            if partes.distance(cabeza) < 10:
                metodo.obtenerPuntaje(metodosJugador.nombreDelJugador(),nivelmax)
                metodo.reiniciarJuego()
                puntos = 0
                texto.clear()
                texto.write(f'Hola {metodosJugador.nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center", font=("impact, 12"))

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
                partes.color("yellow")
            else:
                partes.color(random.choice(coloresCuerpo))
            partes.penup()  # para no dejar rastro cuando se mueva
            # para que el ultimo segmento del cuerpo siga al de adelante
            cuerpoGusanito.append(partes)

            puntos += 1
            if puntos > nivelmax:
                nivelmax = puntos


            texto.clear()
            texto.write(f'Hola {metodosJugador.nombreDelJugador()},    Tus Puntos:{puntos}    Alto Puntaje:{nivelmax}', align="center", font=("impact, 12"))

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


        metodo.mov()
        time.sleep(posponer)


ventanatk.mainloop()




