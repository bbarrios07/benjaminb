
# palabra=input("ingrese una palabra ")

# caract=0
# for i in palabra:
#     print(i)
#     caract=caract+1
# print("su palabra tiene", caract,"caracteres")   
        
# print("la cant de cartacteres es", len(palabra))
# ------------------------------------------------------------------------
lavado=0
clientes=0

while True:
    op=int(input('''seleccione su opcion
                            1.- Cursar pago del lavado
                            2.- Ver ventas diarias
                            3.- Salir
                            '''))

    match op:
        case 1:
            ola=int(input('''seleccione una opcion
                            1.- Full $15.000
                            2.- Standard $10.000
                            3.- Basico $7.000
                            '''))
            match ola:
                case 1:
                    lavado+=15000
                    print("su coche se a lavado con exito")
                    clientes+=1
                    
                case 2:
                    lavado+=10000
                    print("su coche se a lavado con exito") 
                    clientes+=1
                    
                case 3:
                    lavado+=7000
                    print("su coche se a lavado con exito")
                    clientes+=1
                    
        case 2:
            print(f"hoy an venido {clientes} clientes y hemos recaudado {lavado}")
            if ola==1:
                print("el monto mas alto de hoy a sido de $15.000")
            elif ola==2:
                print("el monto mas alto de hoy a sido de $10.000")
            elif ola==3:
                print("el monto mas alto de hoy a sido de $7.000")
        case 3:
            print("que tenga buen dia")
            break