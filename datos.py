# # mostrar posicion de lista

# milista=[1,2,3,4,5,]

# print(milista[2])

# # mostrar elementos de lista


# milista=[1,2,3,4,5,]
# for elemento in milista:
#     print(elemento)


# milista=[1,2,3,4,5,]
# milista.append(6)

# for elemento in milista:
#     print(elemento)

# # insertar texto

# milista=[1,2,3,4,5]
# milista.insert(3,"juan")

# for elemento in milista:
#     print(elemento)

# eliminar elementos

# milista=[1,2,3,'juan',4,5]
# milista.remove("juan")

# for elemento in milista:
#     print(elemento)

# # invertir y ordenar lista

# milista=[5,3,4,1,2,]
# milista.reverse()
# milista.sort(reverse=True)

# for elemento in milista:
#     print(elemento)
from os import system
system("cls")

lista_productos=[]

while True:
    print("mish ")
    print("1.- agregar producto")
    print("2.- eliminar producto")
    print("3.- mostrar todos los productos")
    print("4.- salir")
    op=int(input())
    match op:
        case 1:
            producto=input("ingresar producto: ")
            lista_productos.append(producto)
            print(f"el producto '{producto}' fue agregado correctamente")
            input("presione ENTER para continuar")
            system("cls")
        case 2:
            cont=1
            for i in lista_productos:
                print(f"{cont}._{i}")
                cont+=1

            aux=int(input("cual desea eliminar? "))-1
            lista_productos.pop(aux)
            input("presione ENTER para continuar")
            system("cls")

        case 3:
            cont=1
            for i in lista_productos:
                print(f"{cont}._{i}")
            input("presione ENTER para continuar")
            system("cls")
        case 4:
            break
        case _:
            print("no es una opcion valida")

