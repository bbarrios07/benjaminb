import time
import random
vida=100
violento=30
dinero=0
cliente_molesto=1
golpe_fuerte=1
print("bienvenido a El Heladero Violento")
print("Sos un heladero con poca paciencia, y tenés que lidiar con clientes... algunos más violentos que otros ")
time.sleep(1)
print("tu objetivo es obtener 100$ sin que te terminen mandando al hospital D:")
time.sleep(2)
while dinero<100 and vida>0:
    cliente=random.randint(1,5)
    if cliente==violento:
        op=int(input('''parece que el cliente esta algo molesto
                        que deberia de hacer?
                        1.- tratar de negociar (50%)
                        2.- agarrarse a putazo limpio'''))
        match op:
            case 1:
                probpelea=random.randint(1,2)
                if probpelea==cliente_molesto:
                    print("parece el cliente no quiso negociar...")
                    time.sleep(1)
                    print("tocara agarrarse a putazos nomas")
                    while violento>0:
                        op2=int(input('''que vas a hacer?
                                        1.-cachetada rapida
                                        2.- golpe fuerte (25%)
                                        3.- recuperar vida (-10$)
                                        '''))
                        match op2:
                            case 1:
                                print("haz usado cachetada rapida")
                                violento-=10
                                print("el cliente a recibido 10 de daño")
                                time.slep(0.5)
                            case 2:
                                probgolpe=random.randint(1,4)
                                if probgolpe==golpe_fuerte:
                                    print("le haz dado un combo bien dado al cliente")
                                    violento-=10
                            case 3:
                                if dinero<10:
                                    print("no tienes dinero suficiente para poder comerte tu mercancia :(")
                                else:
                                    print("te haz comido uno de tus helados...")    
                                    time.sleep(1)
                                    print("haz recuperado 15 de vida")
                                    dinero-=10
                            case _:
                                print("selecciona una opcion valida...")
                    if violento<=0:
                        print("dejaste nockout al cliente")
                        dinero+=10
                        print("ganaste 10$")
                    else:
                        print("el cliente te dejo hospitalizado de por vida :,(")
                        print("Perdiste pipipi")
                        break
                elif probpelea!=cliente_molesto:
                    print("has negociado con el cliente exitosamente!")
                    time.sleep(0.5)
                    dinero+=15
                    print("obtienes 15$")
            case 2:
                print("¡te agarras a putazos de una!")
                while violento>0:
                        op2=int(input('''que vas a hacer?
                                        1.-cachetada rapida
                                        2.- golpe fuerte (25%)
                                        3.- recuperar vida (-10$)
                                        '''))
                        match op2:
                            case 1:
                                print("haz usado cachetada rapida")
                                violento-=10
                                print("el cliente a recibido 10 de daño")
                                time.slep(0.5)
                            case 2:
                                probgolpe=random.randint(1,4)
                                if probgolpe==golpe_fuerte:
                                    print("le haz dado un combo bien dado al cliente")
                                    violento-=10
                            case 3:
                                if dinero<10:
                                    print("no tienes dinero suficiente para poder comerte tu mercancia :(")
                                else:
                                    print("te haz comido uno de tus helados...")    
                                    time.sleep(1)
                                    print("haz recuperado 15 de vida")
                                    dinero-=10
                            case _:
                                print("selecciona una opcion valida...")
                if violento<=0:
                    print("dejaste nockout al cliente")
                    dinero+=10
                    print("ganaste 10$")
                else:
                    print("el cliente te dejo hospitalizado de por vida :,(")
                    print("Perdiste pipipi")
                    break
    else:
        print("el cliente se ve amable <3")
        op3=int(input('''que deseas hacer?
                         1.- venderle el helado
                         2.- recuperar vida (-10$)
                         '''))
        match op3:
            case 1:
                print("le vendes un helado al cliente")
                time.sleep(0.5)
                dinero+=20
                print("haz ganado 20$")
                time.sleep(1)
            case 2:
                if dinero<10:
                    print("no tienes dinero suficiente para poder comerte tu mercancia :(")
                else:
                    print("te haz comido uno de tus helados...")    
                    time.sleep(1)
                    print("haz recuperado 15 de vida")
                    dinero-=10
            case _:
                print("selecciona una opcion valida")


if dinero>=100:
    print("haz ganado el juego!")

    