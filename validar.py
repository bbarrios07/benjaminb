

while True:
    try:
        numero=int(input("ingrese valor: "))
        if numero<20 or numero>50:
            print("ERROR, numero ingresado fuera de rango")
        else:
            print("numero ingresado correctamente!")
            break
    
    except ValueError:
        print("ingrese un valor no entero")

for i in range(numero):
    print("algo")

# menu_estructura

while True:
    print("")
    print("")
    print("")
    print("")
    print("")
    op=int(input())
    match op:
        case 1:
            print()
        case 2:
            print()
        case 3:
            print()
        case 4:
            print()
        case _:
            print()




