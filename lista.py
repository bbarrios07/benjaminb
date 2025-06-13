
# #     -5 -4 -3 -2 -1
# numeros=[7,5,33,24,9]
# #      0 1 2  3  4

# print(numeros[-1])

# for numero in numeros:
#     print(numero)

# print(numeros)

# numeros.append(64)

# print(numeros)

# numeros.insert(3,100)

# print(numeros)

# frutas=["manzana", "mango", "membrillo"]

# for fruta in frutas:
#     print(fruta)
# --------------------------------------------------------------------------------
# nombres=[]
# apellidos=[]
# while True:
#     print('''
#          1.- inserte un nombre y apellido
#          2.- mostrar nombres y apellidos
#          3.- buscar nombre
#          4.- Salir
#           ''')
#     op=int(input("seleccione una opcion: "))
#     match op:
#         case 1:
#             nom=input("ingrese un nombre: ")
#             nombres.append(nom)
#             ape=input("ingrese un apellido: ")
#             apellidos.append(ape)
#             print(apellidos)
#         case 2:
#             # c=0
#             # for n in nombres:
#             #     print(nombres[c], apellidos[c])
#             #     c+=1
#             for i in range(len(nombres)):
#                 print(nombres[i], apellidos[i])
#         case 3:
#             nom=input("ingrese un nombre: ")
#             if nom in nombres:
#                 print(f"el nombre {nom} existe")
#             else:
#                 print(f"el nombre {nom} NO existe")
#         case 4:
#             print("saliendo")
#             break
#         case _:
#             print("opcion invalida")
# -------------------------------------------------------------------------

notas=[7.0,5.6,6.3,3.1,7.0,5.9,4.0]

while True:
    try:
        print('''
            1.- Ingresar notas
            2.- Borrar nota
            3.- Mostrar notas
            4.- Sacar promedio, nota mayor y nota menor
            5.- Limpiar todas las notas
            6.- Salir''')
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                    n=float(input("Ingrese la nota: "))
                    notas.append(n)
                    print("la nota se ingreso exitosamente")
            case 2:
                for i, nota in enumerate (notas):
                    print(i+1,".-", nota)
                b=float(input("Que nota desea borrar?: "))
                notas.pop(b-1)
                print("la nota se borro exitosamente")
            case 3:
                print("estas son las notas que hay")
                print(notas)
            case 4:
                c=0
                suma=0
                for nota in notas:
                    suma=suma+nota
                    c+=1
                prom=suma/len(notas)  
                print(prom)  
                print(f"la nota mas alta es", notas[-1])
                print(f"la nota menor es", notas[0])
            case 5:
                notas.clear()
                print("notas borradas")
            case 6:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("ta mal")
# ---------------------------------------------------------------------------------
vero=[
                [3,4],
                [8,9,64,8]
                 ]

print(vero[1][2])