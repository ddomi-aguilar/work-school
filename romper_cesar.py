ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

desencriptado=" " 
#DESENCRIPTAR EL MENSAJE

encriptado=input("ESCRIBE UN MENSAJE: ")
#llave=int(input("Dame la llave en la que deseas encriptar: "))

for llave in range (0,len(ABC)):
    desencriptado=""
    for i in range (0,len(encriptado)):
        posicion=ABC.find(encriptado[i])
        if posicion>=0:
            indice=posicion+llave
            if indice>=26:
                indice=indice-26
            desencriptado+=ABC[indice]    
        else:
            desencriptado+=" "
    print("Llave",llave,"El mensaje desencriptado es: ",desencriptado)