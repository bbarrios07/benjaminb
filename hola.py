
# # declaracion de variables
# nombre="Erika"
# edad=64
# #  ejemplo de concatenacion
# print ("hola",nombre, "y su edad es",edad)

# # declaracion de variables
# print ("ingrese su nombre")
# nombre=input()
# print("ingrese su edad")
# edad=input()
# #  ejemplo de concatenacion
# print ("hola",nombre, "y su edad es",edad)


# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))

# print("el resultado de la multiplicacion es:", n1*n2)

# promedio de 3 numeros

# n1=int(input("ingrese un numero "))
# n2=int(input("ingrese un numero "))
# n3=int(input("ingrese un numero "))

# resultado=(n1+n2+n3)/3
# print("el promedio de los numeros es:", resultado)

# if resultado>=40:
#     print("el alumno aprobo")
# else: 
#     print("el alumno reprobo")



# edad=int(input("ingrese su edad: "))
# if edad>=18:
#     print("usted es mayor de edad" )
# else:
#     print("usted es menor de edad")

# edad=int(input("ingrese su edad: "))
# if edad<12:
#     print("usted es un niño")
# elif edad>=12 and edad<18:
#     print("usted es un adolescente")
# elif  edad>=18 and edad<65:
#     print("usted es un adulto")
# else :
#     print("usted es un viejito")



# for i in range (3):
#    print ("esta es la tabla del ", i)


# cant=input(input("Ingrese la cant de repeticiones "))


# for i in range (cant):
#     print ("repeticion ", i+1)


# nombre=input("ingrese su nombre")
# edad=input("ingrese su edad")

# print("hola", nombre, "su edad es",edad)
# print(f"hola {nombre} su edad es {edad}")

# # para convertir variable en numero
# num=int(input("ingrese un numero"))

# for i in range(11):
#     print(i, "x", num, "=",i*num)

# for i in range(1, 11):
#     for j in range(1, 11):
#      print(i,"x", j, "=",i*j)

# cant=int(input("ingrese la cantidad de notas "))
# total=0
# notasAzules=0
# for i in range(cant):
#     print("ingrese la nota ", i+1)
#     nota=float(input())
#     total=total+nota
#     if nota>=4:
#         notasAzules=notasAzules+1
# prom=total/cant

# print(f"su promedio es {prom}")    
# print(f"la cantidad de notas sobre 4 fue {notasAzules}")


# if prom>=4:
#     print("el alumno aprovo") 
# else:
#     print("el alumno reprobo")



# clave=3344

# password=int(input("ingrese la contraseña :"))

# if password==clave:
#     print("bienvenido al sistema")
# else:
#     print("ERROR, clave invalida")


# for i in range (3):
#   password=int(input("ingrese la contraseña :"))
#   if password==clave:
#     print("bienvenido al sistema")
#     break
# else:
#     print("ERROR, clave invalida")

total=0
for i in range(cant):
    print(" que llevara?"
          "aceituna")


if opcion == 1:
    print("llevate una aceituna")
elif opcion == 2:
    print("llevate una sandia")
elif opcion == 3:
    print("llevate una mandarina")
elif opcion == 4:  
    print("llevate un completo")
