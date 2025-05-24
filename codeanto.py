# import random
# import time
# import sys


# # colores_brillantes_ANSI
# colors = [
#     "\033[1;91m", #rojo_brillante
#     "\033[1;92m", #verde_brillante
#     "\033[1;93m", #amarillo_brillante
#     "\033[1;94m", #azul_brillante
#     "\033[1;95m", #morado_brillante
#     "\033[1;96m", #cian_brillante
#     "\033[1;97m", #blanco_brillante

# ]
# reset = "\033[0m"

# #simbolos_musicales
# music_symbols = [ "♩", "♪", "♫", "♬"]

# def print_lyrics():
#     lines = [
#         "Si yo le salgo por la izquierda",
#         "Se va pa´ la derecha",
#         "No sé lo que le pasa",
#         "Conmigo ella no quiere bailar",
#         "",
#         "Ella me gusta, pero nunca me hace caso",
#         "Ella me mira como si fuera un payaso",
#         "Y, aunque lo intente, al final no tiene caso",
#         "Dime que pasó, ¿cuál es tu rechazo?",
#         "",
#         "Why?",
#         "Me ignoras y te das la vuelta",
#         "Sin siquiera hablarme",
#         "Tell me, why?",
#         "Pero dime como hacer",
#         "Para convencerla a usted",
#         "",
#         "Si yo queria hablarle",
#         "Saludarle",
#         "Conocerla bien",
#         "Yo queria decirle",
#         "que me encanta",
#         "Pero se complica",
#         "Yo no entiendo por qué es tán",
#         "Picky, picky, picky, picky"
#     ]
#     for i, line in enumerate(lines):
#         color = colors[i % len(colors)]
#         symbol = random.choice(music_symbols)
#         print(color, end= "")
#         for char in line:
#             print(char, end="")
#             sys.stdout.flush()
#             time.sleep(0.04)
#         if line.strip() != "":
#             print(f" {symbol}{reset}")
#         else:
#             print(reset)
#         time.sleep(0.25)

#     print("\n\033[1;97m** . . . . ** \033[0m")

# print_lyrics()
# -------------------------------------------------------------------------


# import turtle

# # Configuración de la pantalla
# screen = turtle.Screen()
# screen.bgcolor("white")

# # Configuración de la tortuga
# pen = turtle.Turtle()
# pen.color("red")
# pen.pensize(3)
# pen.speed(3)

# # Función para dibujar la curva del corazón
# def curva():
#     for i in range(200):
#         pen.right(1)
#         pen.forward(1)

# # Función para dibujar el corazón completo
# def corazon():
#     pen.fillcolor("red")
#     pen.begin_fill()
#     pen.left(140)
#     pen.forward(113)
#     curva()
#     pen.left(120)
#     curva()
#     pen.forward(112)
#     pen.end_fill()


# # Llamada a las funciones
# corazon()


# # Ocultar la tortuga
# pen.hideturtle()

# # Mantener la ventana abierta
# turtle.done()

# -------------------------------------------------

# #Programa de Python para dibujar un espiral

# #importamos el módulo de turtle
# import turtle
# #turtle.hideturtle()

# # creamos el fondo
# fondo = turtle.Screen()
# # elegimos el color del fondo
# fondo.bgcolor("white")
# #elegimos el nombre de nuestro lienzo
# fondo.title("Espiral de colores")

# # creamos nuestra tortuga/lapiz
# lapiz = turtle.Turtle()
# #escondemos el puntero
# lapiz.hideturtle()
# #definimos la velocidad del trazo que va de 0 (más rápido) a 10 (más lento)
# lapiz.speed(0)

# #creamos variables para nuestro programa
# colores = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']


# # for loop para dibujar el espiral de colores
# for i in range(555):
#     lapiz.pencolor(colores[i%6])
#     lapiz.width(i//50)
#     lapiz.forward(i)
#     lapiz.left(188)

# #creamos una variable para almacenar la imagen creada
# imagen = turtle.getscreen()
# #creamos un archivo de imagen
# imagen.getcanvas().postscript(file="espiralcolores.eps")

# #termina la execucíon de turtle
# turtle.done()

# -----------------------------------------------------------------

#Programa de Python para dibujar un círculo

#importamos el módulo de turtle
import turtle

# creamos el fondo
fondo = turtle.Screen()
# elegimos el color del fondo
fondo.bgcolor("blue")
## elegimos el nombre de nuestro lienzo
fondo.title("Mi primer círculo en Turtle!")

# creamos nuestra tortuga/lapiz
lapiz = turtle.Turtle()

# Seteamos el color de relleno a rojo
lapiz.fillcolor("green")
lapiz.begin_fill()
 
# Dibujamos el círculo con un radio de 100 pixeles
lapiz.circle(100)

# Paramos el relleno de color y de dibujar
lapiz.end_fill()
turtle.done()