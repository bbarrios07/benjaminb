# Juego

# Reglas o requisitos:
# Hay dos jugadores: Jugador y el boss.

# El jugador tiene 100 de vida.
# El jefe final tiene 150 de vida.

# Cada ronda:
# El jugador ataca primero:
# Elige entre 3 opciones:

# Golpe rápido (10 de daño)

# Golpe fuerte (25 de daño, pero con 50% de probabilidad)

# Curarse (+15 de vida, máximo 100)

# Luego el jefe ataca y hace entre 10 y 20 de daño aleatorio al jugador.
# El juego muestra:
# Vida del jugador y del jefe después de cada ronda.
# Cuántas rondas han pasado.
# El combate sigue hasta que uno de los dos llegue a 0 o menos de vida.
# Al final, mostrar:
# Quién ganó.
# Cuántas rondas duró el combate.
# # ---------------------------------------------------------------------
# import random
# jugador=100
# boss=150
# ronda=0

# while jugador>=0 and boss>=0:
    
#         op=int(input('''que vas a hacer?
#                         1.- ataque rapido
#                         2.- golpe fuerte (50%)
#                         3.- curarse
#                         '''))
#         match op:
#             case 1:
#                 print("jugador a usado ataque rapido")
#                 print("¡el boss a recibido 10 de daño!")
#                 boss-=10
#                 ronda+=1
#                 print(f"el boss ahora tiene {boss} % de vida")
#             case 2:
#                 print("jugador a usado golpe fuerte")
#                 golpe=random.randint(1,2)
#                 if golpe==2:
#                     print("GOLPE FUERTE")
#                     print("¡el boss a recibido 25 de daño!")
#                     boss-=25
#                     ronda+=1
#                     print(f"el boss ahora tiene {boss} % de vida")
#                 else:
#                     print("el jugador a fallado!!!")
#                     ronda+=1
#             case 3:
#                 print("el jugador se a curado ")
#                 if jugador==100:
#                     print("parece que el jugador ya tiene el maximo de vida... que pena :()")
#                 else:
#                     print("el jugador se a curado 15 de vida!")
#                     jugador+=15
#                     ronda+=1
#                     print(f"el jugador ahora tiene {jugador} % de vida")
#             case _:
#                 print("selecciona una opcion valida...")
#         print("turno del boss")
#         probfallo=random.randint(1,3)
        
#         if probfallo==3:
#             print("el boss CONTRAATACA!!")
#             ataqueb=random.randint(10,20)
#             print(f"el boss te a hecho {ataqueb} de daño!!")
#             jugador-=ataqueb
#             print(f"el jugador ahora tiene {jugador} % de vida")
#             ronda+=1
#         else:
#             print("el boss fallo :(")
#             ronda+=1
    
# if jugador<=0 or boss<=0:
#     if boss<=0:
#         print("el jugador a ganado :D!!")
#         print(f"el jugador quedo con {jugador} % de vida")
#         print(f"el juego a durado {ronda} rondas")
#     elif jugador<=0:
#         print("el jugador a perdido :,v")
#         print(f"el boss quedo con {boss} % de vida")
#         print(f"el juego a durado {ronda} rondas")
#         print("suerte para la proxima <3")

# --------------------------------------------------------------------
# 

while True:
    op=int(input('''ola, esto es un menu
                    1.-a poco si tilin?'''))




