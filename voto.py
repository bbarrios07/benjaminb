votantes=int(input("ingrese cantidad de votantes: "))

kaiser=0
nose=0

for i in range (votantes):
    voto=int(input("ingrese un voto: kaiser 1, nose 2 "))
    if voto==1:
        kaiser=kaiser+1
    elif voto==2:
        nose=nose+1
    else:
        print("Error, selecione un voto valido")

print("los votos de kaiser son", kaiser)
print("los votos de kaiser son", nose)

if kaiser>nose:
    print("gano kaiser")
elif kaiser==nose:
    print("es un empate")
else:
    print("gano nose")

