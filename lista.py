
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

nombres=[]
apellidos=[]
while True:
    print('''
         1.- inserte un nombre y apellido
         2.- mostrar nombres y apellidos
         3.- buscar nombre
         4.- Salir
          ''')
    op=int(input("seleccione una opcion: "))
    match op:
        case 1:
            nom=input("ingrese un nombre: ")
            nombres.append(nom)
            ape=input("ingrese un apellido: ")
            apellidos.append(ape)
            print(apellidos)
        case 2:
            # c=0
            # for n in nombres:
            #     print(nombres[c], apellidos[c])
            #     c+=1
            for i in range(len(nombres)):
                print(nombres[i], apellidos[i])
        case 3:
            nom=input("ingrese un nombre: ")
            if nom in nombres:
                print(f"el nombre {nom} existe")
            else:
                print(f"el nombre {nom} NO existe")
        case 4:
            print("saliendo")
            break
        case _:
            print("opcion invalida")