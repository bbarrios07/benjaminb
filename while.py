# while= mientras


# num=0

# while num<=5:
#     print(num)
#     num+=1

# import time
# num= 10
# while num>=0:
#     print(num)
#     time.sleep(1)
#     num-=1

# resp="no"

# while resp!="si":
#    resp=input ("desea salir del programa? ")
# ---------------------------------------------------------------------------------------
# clave=3344
# intentos=3
# contraseña=int(input("ingrese su contraseña "))

# while clave!=contraseña:
#     intentos-=1
#     print("quedan ", intentos, " intentos")
#     print("Error, clave invalida")
#     contraseña=int(input("ingrese su contraseña "))
    
#     if intentos==1:
#         break
    
# if clave==contraseña:
#     print("clave aceptada")
# else: 
#     print("sistema bloqueado")
 

# num=1

# while num!=0:
#     num=int(input("ingrese un numero (0 para salir) "))
#     if num % 2==0:
#         print(f"el numero {num} es par")
#     else:
#          print(f"el numero {num} es impar")   


# import random
# randy=random.randint(1,10)
# print(randy)

# import random
# numAzar=random.randint(1,30)
# print (numAzar)
# if numAzar>=20:
#     print("puede pasar")
# else:
#     print("le falta puntaje")


# import random
# numAzar=random.randint(1,50)
# num=0
# num=int(input("ingrese un numero "))
# while num!=numAzar:
#  if num>numAzar:
#     print("el numero a adivinar es menor")
#     num=int(input("ingrese otro numero "))
#  elif num<numAzar:
#     print("el numero a adivinar es mayor")
#     num=int(input("ingrese otro numero "))
 
# if num==numAzar:
#   print("felicidades pinche puto")

# ----------------------------------------------------------
# import random
# numAzar=random.randint(1,6)
# barril=int(input("ingrese numero del barril: "))
# while barril!=numAzar:
#     print("fogueo")
#     barril=int(input("ingrese numero del barril: "))

# print("¡BANG!")     

# -----------------------------------------------------------------
# import random
# numAzar=random.randint(1,6)
# barril=int(input("ingrese numero del barril: "))
# while barril!=numAzar:
#     print("Hola Mundo")
    
#     barril=int(input("ingrese numero del barril: "))

# print("¡ADIOS MUNDO!")     
# -----------------------------------------------------------
while True:
    try:
        opcion=int(input('''
                            seleccione una opcion con un numero entero
                            1.- Opcion 1
                            2.- Opcion 2
                            3.- Opcion 3
                            4.- Salir
                         '''))
        match opcion:
            case 1:
                print("a seleccionado la opcion 1")
            case 2:
                print("a seleccionado la opcion 2")
            case 3:
                print("a seleccionado la opcion 3")
            case 4:
                print("saliendo...")
                break
            case _:
                print("opcion no valida")
    except Exception:
        print("solo se pueden ingresar numeros enteros")

total=0
cantart=0


while True:
    try:
        opcion=int(input('''Carrito de compras
                            seleccione una opcion con un numero entero
                            1.- Comprar frutas
                            2.- Comprar verduras
                            3.- pagar
                            4.- Salir
                         '''))
        match opcion:
            case 1:
                print("a seleccionado la opcion 1")
                while True:
                    try:
                        opcion=int(input('''
                                            seleccione una opcion con un numero entero
                                            1.- Frutilla $1500
                                            2.- Pera $1200
                                            3.- Manzana $1300
                                            4.- Volver al menu
                                        '''))
                        match opcion:
                            case 1:
                                print("a seleccionado Frutilla")
                                total+=1500
                                cantart+=1
                            case 2:
                                print("a seleccionado Pera")
                                total+=1200
                                cantart+=1
                            case 3:
                                print("a seleccionado Manzana")
                                total+=1300
                                cantart+=1
                            case 4:
                                print("Volviendo...")
                                break
                            case _:
                                print("opcion no valida")
                                    
                    except Exception:
                        print("solo se pueden ingresar numeros enteros")
                    print("Tu total hasta hora es de", total)
            case 2:
                print("a seleccionado la opcion 2")
            case 3:
                print("a seleccionado la opcion 3")
            case 4:
                print("saliendo...")
                break
            case _:
                print("opcion no valida")
    except Exception:
        print("solo se pueden ingresar numeros enteros")
