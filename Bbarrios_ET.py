productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
        '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
        'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
        'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
        'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
        '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
        '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
        'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
 'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
 'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

def stock_marca():
    marca=int(input('''que marca busca?
                        1.-HP
                        2.-Lenovo
                        3.-Asus
                        4.-Dell
                        '''))
    match marca:
        case 1:
            print("quedan 31 HP")
        case 2:
            print("quedan 43 Lenovo")
        case 3:
            print("quedan 3 Asus")
        case 4:
            print("queda 1 Dell")
        case _:
            print("ingresa una opcion valida...")
            




def búsqueda_precio():
    min=int(input("Ingrese precio minimo: "))
    max=int(input("ingrese precio maximo: "))






def actualizar_precio(dict):
    for key,value in dict.items():
        print(key, value)
        act=input("que modelo actualizara?: ")
        stock[act]
        precio=int(input("cual va a hacer el nuevo precio?: "))
        stock[act][precio]
        

while True:
    try:
        op=int(input('''*** MENU PRINCIPAL ***
                1. Stock marca.
                2. Búsqueda por precio.
                3. Actualizar precio.
                4. Salir.
                Ingrese opcion: '''))
    except:
        print("solo numeros enteros...")
        op=int(input('''*** MENU PRINCIPAL ***
                1. Stock marca.
                2. Búsqueda por precio.
                3. Actualizar precio.
                4. Salir.
                Ingrese opcion: ''')) 

    match op:
        case 1:
            stock_marca()
        case 2:
            búsqueda_precio()
        case 3:
            actualizar_precio(stock)
        case 4:
            print("Programa finalizado")
            break
        case _:
            print("Ingrese una opcion valida...")
