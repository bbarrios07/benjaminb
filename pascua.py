import random
while True:
    try:
        cantN=int(input("cuantos niños van a buscar huevitos? "))

        print("solo numeros enteros")
    noob=0
    master=0
    legend=0
    top=0
    for n in range(cantN):
        cantH=random.randint(5,30)
        print(f"El niño numero {n+1} encontro {cantH} huevos")
        if cantH>top:
            top=cantH
        if cantH<12:
            noob+=1
        elif cantH>=12 and cantH<=24:
            master+=1
        else:
            legend+=1
    print("la cantidad del grupo noob es", noob) 
    print("la cantidad del grupo master es", master) 
    print("la cantidad del grupo legend es", legend) 
    print("la mayor cantidad de huevos encontrada por un niño fue", top) 
