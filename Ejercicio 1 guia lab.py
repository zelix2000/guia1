#Ejercicio 1 

def rut():
    N = [2,3,4,5,6,7,2,3,4,5,6,7]
    Z = input("Ingrese RUT sin verificador: ")
    Z = Z[::-1]
    A = 0
    d = 0
    H = 12
    suma = 0
    
    while A < len(Z):
        d = int(Z[A])*int(N[A])
        suma = suma + d
        A = A + 1
    print (suma)
    v = 11 - (suma % 11)
    
    if 0 < v < 10:
        H = v
    elif v == 11:
        H = 0
    elif v == 10:
        str(H)
        H = "K"
        
    print ("El digito verificador es: ", H)
    
rut()
    
