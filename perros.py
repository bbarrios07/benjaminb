# import random

# cantperros=int(input("cuantos perros hay? "))
# cantconejos=int(input("cuantos conejos MINIMO tienen que traer? "))

# filete=0
# nofilete=0
# perros=random.randint (1,25)
# for i in range (cantperros):
#     print(f"el perro {i+1} trajo {perros} conejos")
#     perros=random.randint (1,25)
#     if perros<cantconejos:
#         print("el perro no tiene filete :(")
#         nofilete=nofilete+1
#     elif perros>cantconejos:
#         print("el perro tiene filete :)")
#         filete=filete+1




# print(f"{filete} perros tuvieron filete")
# print(f"{nofilete} perros no tuvieron filete")

# ---------------------------------------------------------------------
import random, time


while True:
    try:
        perros=int(input("cuantos perros van a la caza? "))
        while perros<1:
            print("solo valores enteros positivos")
            perros=int(input("cuantos perros van a la caza? "))
        cuota=3
        pCumplen=0
        for p in range (perros):
            time.sleep(1)
            conejos=random.randint(0,6)
            if conejos>=cuota:
                print(f"el perro {p+1} capturo {conejos} conejos")
                print("Se gano un filete")
                pCumplen+=1
            else:
                print(f"el perro {p+1} capturo {conejos} conejos")
                print("Se gano un filete")    
        print(pCumplen, "perros llegaron a la cuota")      
        print(perros-pCumplen, "perros no llegaron a la cuota")
        break
    except Exception:
        print("Solo debe poner numeros enteros") 