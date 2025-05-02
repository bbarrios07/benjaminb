import time
import random
meta=30
turno=1
j1=0
j2=0
while j1>=meta or j2>=meta:
    if turno%2==0:
        print("turno de j1")
        time.sleep (1)
        dado=random.randint (1,5)
        print(f"el j1 saco {dado}")
        j1=j1+dado
        print(f"Avanza hasta la casilla {j1}")
        turno=turno+1
    else:
        print("turno de j2")
        time.sleep (1)
        dado=random.randint (1,5)
        print(f"el j2 saco {dado}")
        j2=j2+dado
        print(f"Avanza hasta la casilla {j2}")
        turno=turno+1
if j1>=meta:
    print("gano el j1")
elif j2>=meta:
    print("gano j2")