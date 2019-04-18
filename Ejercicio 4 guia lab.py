#Ejercicio 4 

nombre=input("ingrese el nombre del deportista: ")
d=float(input("igrese la dificultad del clavado: "))
jueces=7
x=0
i=0
I=0
puntajes=[]
for i in range(0,jueces) :
    x=float(input("puntaje obtenido: "))
    x=x+I
    puntajes.append(x)
    if I==0:
        I=1/2
puntajes.sort()

puntajes.pop(-1)

puntajes.pop(0)

r=(puntajes[0]+puntajes[1]+puntajes[2]+puntajes[3]+puntajes[4])*(3/5)
r=r*d
print("el puntaje es: ",r)

            
    
