
# def suma():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     print (n1+n2)


# def suma_ret():
#     n1=int(input("ingrese un numero: "))
#     n2=int(input("ingrese otro numero: "))
#     return (n1+n2)


# def suma_arg(n1,n2):
#     print(n1+n2)

# def suma_arg_ret(n1,n2):
#     return (n1+n2)

# nun1=int(input("ingrese un numero: "))
# num2=int(input("ingrese otro numero: "))
# suma_arg(8,9)


# suma()
# suma_ret

# def iva(n):
#     return n*1.19

# def descuento(precio,porc):
#     return precio*(porc/100)

# productos=[
#     {"nombre":"lapiz", "precio":400},
#     {"nombre":"goma", "precio":200},
#     {"nombre":"estuche", "precio":1600}
# ]

# print(productos[1]["precio"])


# '''el arituculo lapiz tiene un precio de 400'''

# for item in productos:
#     print(f"el articulo {item["nombre"]} tiene un precio de {item["precio"]}")

productos=[
    {"nombre":"tumamita", "precio":20000},
    {"nombre":"coquita", "precio":1750},
    {"nombre":"completito", "precio":1500}

]

while True:
    op=int(input('''
                1.- Agregar articulo
                2.- Borrar articulo
                3.- Actualizar articulo
                4.- Mostrar listado de articulos
                5.- Salir
                '''))   
    match op:
        case 1:
            produc=input("ingrese un producto ")
            precio=int(input("ingresa el precio "))
            tulita={"nombre": produc, "precio": precio}
            productos.append(tulita)
        case 2:
            for n,producto in enumerate(productos):
                print(n+1, productos["nombre"], producto["precio"])
            borrar=int(input("que articulo desea borrar? "))
            productos.pop(borrar-1)

        case 3:
            for n,producto in enumerate(productos):
                print(n+1, producto["nombre"], producto["precio"])
            act=int(input("que articulo desea actualizar? "))
            nombre=input("nombre del articulo: ")
            precio=int(input("precio del producto: "))
            productos[act-1]["nombre"]=nombre
            productos[act-1]["precio"]=precio
        case 4:
            for n,productos in enumerate(productos):
                print(n+1, productos["nombre"], productos["precio"])
        case 5:
            print("saliendo...")
            break
        case _:
            print("seleccione una opcion valida")