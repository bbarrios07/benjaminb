
# import random
# # intentos=2
# # num=0
# # Numadivinar=int(random.randint (1,50))

# # while Numadivinar!=num or intentos==0:
# #     print("Ingrese un numero a adivinar")
# #     num=int(input())
# #     if num>Numadivinar:
# #         print("el numero a adivinar es menor")
# #         intentos=intentos-1
# #     elif num<Numadivinar:
# #         print("el numero a adivinar es mayor")
# #         intentos=intentos-1
    
# # if intentos==0:
# #     print("te has quedado sin intentos")
# #     print(f"el numero a encontrar era {Numadivinar}")
# # elif num==Numadivinar:
# #     print("felicidades!")
# # ------------------------------------------------------------------------------------------
# # empanada=0
# # carlos=0

# # votantes=int(input("cuantos votantes hay? "))      

# # for i in range (votantes):
# #     voto=int(input("ingrese un voto: 1.-empanadas el momero, 2.-carlos "))
# #     if voto==1:
# #         empanada=empanada+1
# #     elif voto==2:
# #         carlos=carlos+1
# #     else:
# #         print("ERROR, selecciona una wea valida")
    
# # if empanada<carlos:
# #     print("gano carlos")
# # else:
# #     print("gano empanadas el momero")



# # print("carlos", carlos)
# # print("empanadas el momero", empanada)
# # -------------------------------------------------
# import sys
# print(" hola, que va a llevar? ")
# boleta=0
# productos=0
# Pikachu=0
# Otaku=0
# Pulpo=0
# Anguila=0
# descuento=10
# code="soyotaku"
# codigo="o"
# while codigo!="x":
#     op=int(input('''seleccione su opcion
#                             1.- Pikachu Roll $4500
#                             2.- Otaku Roll $5000
#                             3.- Pulpo Venenoso $5200
#                             4.- Anguila electrica Roll $4800
#                             5.- Salir
#                             '''))
#     match op:
#         case 1:
#             print("a seleccionado un Pikachu Roll")
#             boleta+=4500
#             productos+=1
#             Pikachu+=1
#         case 2:
#             print("a seleccionado un Otaku Roll")
#             boleta+=5000
#             productos+=1
#             Otaku+=1
#         case 3:
#             print("a seleccionado un Pulpo Venenoso")
#             boleta+=5200
#             productos+=1
#             Pulpo+=1
#         case 4:
#             print("a seleccionado una Anguila electrica Roll")
#             boleta+=4800
#             productos+=1
#             Anguila+=1
#         case 5:
#             codigo=str(input("tienes algun codigo de descuento? (si no escriba X) "))
#             if codigo==code:
#                 print("codigo canjeado")
#                 print(" descuento del 10%")
#                 boletaa=boleta*descuento/100
#                 codigo=str(input(""))
#                 break
#             elif codigo!=code:
#                 print("codigo invalido")
#                 print("desea reintentar? (si no escriba X)")  
#             a

# print(" su boleta es la siguiente")
# print(f"lleva {productos} productos ")
# print(f'''
# Pikachu Roll: {Pikachu}
# Otaku Roll: {Otaku}
# Pulpo Venenoso: {Pulpo}
# Anguila electrica Roll: {Anguila}
# Descuento: {boletaa}
# Total a pagar: {boleta-boletaa}
# ''')

# print("vuelva pronto <3")               
                    
# ---------------------------------------------------------------
deuda=100000


while True:
    op=int(input(""))
    match op:
        case 1:
            print("Guatona guatona culia fea")
        case 2:
            print("tumamita")