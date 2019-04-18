#Ejercicio 3 

x = int(input("ángulo 1: "))
y = int(input("ángulo 2: "))
z= 180 - (x+y)

if x == 90 or y == 90 or z==90:
    print("triángulo rectángulo")
elif x < 90 and y < 90 and z < 90:
    print("triángulo acutángulo")
elif x > 90 or y > 90 or z > 90:
    print("triángulo obtusángulo")