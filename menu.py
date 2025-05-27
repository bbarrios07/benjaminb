import time
usuario1=None
usuario2=None
usuario3=None
contraseña1=None
contraseña2=None
contraseña3=None

def menu():
    while True:
        try:
            inicio=int(input('''
                    Seleccione una opcion 
                        1.- Realizar llamada
                        2.- Enviar correo electronico
                        3.-Cerrar sesion
                         '''))
            break
        except Exception:
            print("Solo numeros validos")
        try:
            match inicio:
                case 1:
                    print("ingrese el numero (debe empezar por 9 y debe tener 9 digitos)")
                    celular=input()
                case 2:
                    print("ingrese el correo ")
                case 3:
                    print("cerrando sesion...")
                    time.sleep(1)
                    break
        except Exception:
            print("solo numeros validos")



while True:
    while True:
        try:
            op=int(input('''
                    Seleccione una opcion 
                        1.- inicio sesión
                        2.-registrar usuario
                        3.-Salir
                         '''))
            break
        except Exception:
            print("Solo numeros enteros")

    match op:
        case 1: 
            if usuario1==None:
                print("no hay ningun usuario creado") 
                print("porfavor cree uno")
            else:
                try:
                    menucito=int(input(f'''
                                    Seleccione su usuario
                                        1.-{usuario1}
                                        2.-{usuario2}
                                        3.-{usuario3}
                                        '''))
                    match menucito:
                        case 1:
                            clave=input("ingrese su contraseña ")
                            if clave!=contraseña1:
                                    print("contraseña incorrecta, vuelva a intentar")
                                    clave=input("ingrese su contraseña ")
                            menu()
                        case 2:
                            if usuario2==None:
                                print("no hay nada :( ")
                            else:
                                clave=input("ingrese su contraseña ")
                                if clave!=contraseña2:
                                    print("contraseña incorrecta, vuelva a intentar")
                                    clave=input("ingrese su contraseña ")
                                menu()
                        case 3:
                            if usuario3==None:
                                print("no hay nada :(")
                            else:
                                clave=input("ingrese su contraseña ")
                                if clave!=contraseña3:
                                    print("contraseña incorrecta, vuelva a intentar")
                                    clave=input("ingrese su contraseña ")
                                menu()
                except Exception:
                    print("solo numeros validos")

                        

        case 2:
            if usuario1==None and contraseña1==None:
                usuario1=input("cual sera su usuario? ")
                contraseña1=input("cual sera su contraseña? ")
                clave=contraseña1
            elif usuario2==None and contraseña2==None:
                usuario2=input("cual sera su usuario? ")
                contraseña2=input("cual sera su contraseña? ")
                clave=contraseña2
            elif usuario3==None and contraseña3==None:
                usuario3=input("cual sera su usuario? ")
                contraseña3=input("cual sera su contraseña? ")
                clave=contraseña3
            else:
                print("ya tiene 3 usuarios creados")

        case 3:
            print("Saliendo...")
            break
        case _:
            print("opcion invalida")