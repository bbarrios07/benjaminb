nombre=input("ingrese su nombre: ")
print("Mucho gusto", nombre, "que va a llevar?")
boleta=0
while True:
    op=int(input('''seleccione su opcion
                            1.- coca cola $2000
                            2.- ramitas $1500
                            3.- chocolate $950
                            4.- Harina $3000
                            5.- Salir
                            '''))

    match op:
        case 1:
            cant=int(input("cuantos va a llevar?"))
            if cant==1:
                boleta=boleta+2000
                print(boleta)
            elif cant==2:
                boleta=boleta+4000
                print(boleta)
            elif cant==3:
                boleta=boleta+6000
                print(boleta)
            elif cant==4:
                boleta=boleta+8000
                print(boleta)
        case 2: 
         cant=int(input("cuantos va a llevar?"))
         if cant==1:
               boleta=boleta+1500
               print(boleta)
         elif cant==2:
                boleta=boleta+3000
                print(boleta)
         elif cant==3:
                boleta=boleta+4500
                print(boleta)
         elif cant==4:
                boleta=boleta+6000
                print(boleta)

