

# # dic={
# #     "nombre":"mel broks",
# #     "numero": 945453443,
# #     "casado": True
# # }

# # print(dic)

# # for key,value in dic.items():
# #     print(key, value)

# # dic["ciudad"]="talca"

# # for key,value in dic.items():
# #     print(key, value)

# # dic["casado"]=False

# # for key,value in dic.items():
# #     print(key, value)
# # ---------------------------------------------------
# frutas={
#     "sandia": 3000,
#     "manzana": 1500,
#     "naranja": 1000
# }
# print(frutas)


# while True:
#     op=int(input('''
#             1.- Ingresar fruta y precio
#             2.- Actualizar precio
#             3.- Borrar fruta y precio
#             4.- mostrar todas las frutas y precios
#             5.- comprar
#             6.-Salir
#              '''))
#     match op:
#         case 1:
#             fruta=input("ingrese una fruta ")
#             precio=int(input("ingresa el precio "))
#             frutas[fruta]=precio
#         case 2:
#             print("que precio desea modificar?")
#             for key,value in frutas.items():
#                 print(key,value)
#             b=float(input(""))
#             frutas.pop(b-1) 
#         case 3:
#             print("")
#         case 4:
#             for key,value in frutas.items():
#                 print(key,value)           
#         case 5:
#             print("")
#         case 6:
#             print("saliendo...")
#             break
#         case _:
#             print("opcion invalida")

# ------------------------------------------------------------------------------

juegos={
    1:{"nombre": "mario", "precio": 50000, "consola": "switch"},
    2:{"nombre": "zelda", "precio": 40000, "consola": "switch"},
    3:{"nombre": "csgo2", "precio": 15000, "consola": "pc"}
}

def mostrar(juegos):
    for j, dict in juegos.items(juegos):
        print(j, dict)


def valida_precio(precio):
    if precio>=8000 and precio<=100000:
        return True
    else:
        return False
    

def valida_nombre(nombre):
    esp=False
    if nombre[-1]!=" " and nombre[0]!=" ":
        for l in nombre:
            if l==" ":
                return True
    else:
        return False