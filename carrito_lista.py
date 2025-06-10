
productos=[]
precios=[]
carrito=[]


while True:
    op=int(input('''
                1.- ingresar productos
                2.- Comprar (sub menu)
                3.- Crear boleta
                4.- Salir
                '''))
    match op:
        case 1:
            print("que va a llevar?")

        case 2:
            print("")
        case 3:
            print("")
        case 4:
            print("hasta luego")
            break
        case _:
            print("opcion invalida")