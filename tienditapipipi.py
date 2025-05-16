boleta=0
nombre="cliente"
op=0
while op!=4:
    op=int(input('''seleccione su opcion
                            1.- ingrese su nombre
                            2.- Comprar
                            3.- Sacar boleta
                            4.- Salir
                            '''))

    match op:
        case 1:
            nombre=input("cual es su nombre ")
        case 2:
              op=int(input('''seleccione lo que llevara
                            5.- coca cola $2000
                            6.- ramitas $1500
                            7.- chocolate $950
                            8.- Harina $3000
                            9.- Salir
                            '''))
    while op!=9:
     match op:
        case 5:
            cant=int(input("cuantos va a llevar? "))
            if cant==1:
                boleta=boleta+2000
                
            elif cant==2:
                boleta=boleta+4000
               
            elif cant==3:
                boleta=boleta+6000
                
            elif cant==4:
                boleta=boleta+8000
                
        case 6: 
         cant=int(input("cuantos va a llevar? "))
         if cant==1:
               boleta=boleta+1500
               
         elif cant==2:
                boleta=boleta+3000
                
         elif cant==3:
                boleta=boleta+4500
                
         elif cant==4:
                boleta=boleta+6000
                
        case 7:
              cant=int(input("cuantos va a llevar? "))
              if cant==1:
               boleta=boleta+950
               
              elif cant==2:
                boleta=boleta+1900
                
              elif cant==3:
                        boleta=boleta+2850
                        
              elif cant==4:
                        boleta=boleta+3800
                        
        case 8:
              cant=int(input("cuantos va a llevar? 1"))
              if cant==1:
               boleta=boleta+3000
               
              elif cant==2:
                boleta=boleta+6000
                
              elif cant==3:
                        boleta=boleta+9000
                        
              elif cant==4:
                        boleta=boleta+12000
                        
        case 9: 
               ola               
        case 3:
              boleta=boleta*1.9
              print("su boleta es de", boleta)
        case 4:
             print("vuelva pronto",nombre, ":)")
             break
     break             
     
             


        

