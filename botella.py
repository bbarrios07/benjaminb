botella=600
sed=True
import time
import random 

while botella>=0 and sed:
    print("glu, glu")
    botella-=random.randint(20,60)
    print("queda", botella)
    resp=input("aun tiene sed? (si/no) ")
    if resp=="no":
        sed=False
    time.sleep(1)


# chocolate=1

# if chocolate==1:
#     print("hay chocolate")
# else:
#     print("no hay chocolate")


