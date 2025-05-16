import colorama
from colorama import Fore

cant=0
totalg=0
cant=int(input("ingrese cantidad de alumnos "))
for i in range (cant):
   
    print(Fore.CYAN, "ingrese la cantidad de notas del alumno", i+1)
    notas=int(input())
    total=0
    for e in range (notas):
        nota=int(input("ingrese la nota "))
        total=total+nota
        
    total=total/notas    
    print("el promedio de el alumno",i+1, "es de ",total)
    if total<=4.0:
        print(f"el alumno {i+1} desaprobo")
        totalg=totalg+total
    elif total>=4.0:
        print(f"el alumno {i+1} aprobo")
        totalg=totalg+total
promg=totalg/cant
print("el promedio general es de",promg)