
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

edad=int(input("ingrese su edad: "))
if edad<12:
    print("usted es un niño")
elif edad>=12 and edad<18:
    print("usted es un adolescente")
elif  edad>=18 and edad<65:
    print("usted es un adulto")
else :
    print("usted es un viejito")
