import random
import time
import sys


# colores_brillantes_ANSI
colors = [
    "\033[1;91m", #rojo_brillante
    "\033[1;92m", #verde_brillante
    "\033[1;93m", #amarillo_brillante
    "\033[1;94m", #azul_brillante
    "\033[1;95m", #morado_brillante
    "\033[1;96m", #cian_brillante
    "\033[1;97m", #blanco_brillante

]
reset = "\033[0m"

#simbolos_musicales
music_symbols = [ "♩", "♪", "♫", "♬"]

def print_lyrics():
    lines = [
        "Si yo le salgo por la izquierda",
        "Se va pa´ la derecha",
        "No sé lo que le pasa",
        "Conmigo ella no quiere bailar",
        "",
        "Ella me gusta, pero nunca me hace caso",
        "Ella me mira como si fuera un payaso",
        "Y, aunque lo intente, al final no tiene caso",
        "Dime que pasó, ¿cuál es tu rechazo?",
        "",
        "Why?",
        "Me ignoras y te das la vuelta",
        "Sin siquiera hablarme",
        "Tell me, why?",
        "Pero dime como hacer",
        "Para convencerla a usted",
        "",
        "Si yo queria hablarle",
        "Saludarle",
        "Conocerla bien",
        "Yo queria decirle",
        "que me encanta",
        "Pero se complica",
        "Yo no entiendo por qué es tán",
        "Picky, picky, picky, picky"
    ]
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        symbol = random.choice(music_symbols)
        print(color, end= "")
        for char in line:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(0.04)
        if line.strip() != "":
            print(f" {symbol}{reset}")
        else:
            print(reset)
        time.sleep(0.25)

    print("\n\033[1;97m** . . . . ** \033[0m")

print_lyrics()