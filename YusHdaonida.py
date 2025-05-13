


def suma():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la suma es ", n1+n2)
def resta():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la resta es ", n1-n2)
def multiplicacion():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print("el resultado de la multiplicacion es ", n1*n2)
def divicion():
    try:
        n1=int(input("ingrese un numero: "))
        n2=int(input("ingrese otro numero: "))
        print("el resultado de la divicion es ", n1/n2) 
    except ZeroDivisionError as nombre_de_exepcion:
        print(f"se produjo una expecion: {nombre_de_exepcion}")

def calcu():
    while True:
        op=int(input('''seleccione su opcion
                    1.- Suma
                    2.- Resta
                    3.- Multiplicacion
                    4.- Divicion
                    5.- Salir
                    '''))


        match op:
            case 1:
                print("Suma")
                suma()
            case 2:
                print ("Resta")
                resta()
            case 3:
                print ("Multiplicacion")
                multiplicacion()
            case 4:
                print("Divicion")

                divicion()
            case 5:
                print("nos vimos giles")
                break
            case _:
                print("Opcion Invalida")
calcu()