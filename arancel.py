# arancel=200000
# descuento=0
# total=0
# print('''
#     1.- La florida 20%
#     2.- la pintana 30%
#     3.- Puente Alto 25%
#     4.- San Joaquin 15%
#       ''')
# com=int(input("seleccione una comuna: "))
# if com==1:
#     descuento=descuento+20
# elif com==2:
#     descuento=descuento+30
# elif com==3:
#     descuento=descuento+25
# elif com==4:
#     descuento=descuento+15

# print("ingrese su grupo familiar (usted incluido) ")
# grupo=int(input(""))
# if grupo==1:
#     descuento=descuento+2
# elif grupo<=4 and grupo>=2:
#      descuento=descuento+3
# else:
#      descuento=descuento+4

# total=arancel/100*descuento
# print(f"el descuento es de {round (total)}")
# arancel=arancel-total
# print(f"el total a pagar es {round (arancel)}")
# ----------------------------------------------------------------------------------------------------

# credito=0
# print("cuanto es su cantidad de ingresos?")
# print("1.- 500.000 a 1.000.000, 2.- 1.000.001 a 1.500.000, 3.- de 1.500.001 o más")
# resp=int(input())
# if resp==1:
#     credito=credito+300000
# elif resp==2:
#     credito=credito+650000
# elif resp==3:
#     credito=credito+1000000

# print("cual es su nivel educacional?")
# print("1.- Basica, 2.- Media, 3.- Superior")

# resp=int(input())
# if resp==1:
#     credito=credito*1
# elif resp==2:
#     credito=credito*1.3
# elif resp==3:
#     credito=credito*1.5
    
# print("su nacionalidad es chilena o extranjero?")
# print("1.- Chilena, 2.- Extranjero")
# resp=int(input())
# if resp==1:
#     credito=credito+300000

# print(f"su credito es de {round(credito)}")
# ------------------------------------------------------------------------
import random

print("ingrese un numero")
num1=int(input())
print("ingrese otro numero (que sea mayor que el anterior)")
num2=int(input())
if num2<num1:
    print("que te dije >:()")
    print("ingrese otro numero (que sea mayor que el anterior)")
    num2=int(input())
numrandom=random.randint(num1,num2)
# for i in range (numrandom):
#     print("▄"*numrandom)
print("▄"*numrandom)