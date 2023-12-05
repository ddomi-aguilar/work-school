
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encriptado=[]
desencriptado=[]

#MENU
print("CIRCULO CESAR")
print("1)Encriptar")
print("2)Desencriptar")
op=int(input("¿Que es lo que quieres hacer?-> "))

#ENCRIPTAR EL MENSAJE
if op==1:
    msg=input("Escribe la palabra/frase a encriptar: ").upper()
    llave=int(input("Dame la llave en la que deseas encriptar: "))
    for i in range (0,len(msg)):
        posicion=ABC.find(msg[i])
        indice=llave+posicion
        if indice>=26:
            indice=indice-26
        encriptado.append(ABC[indice])        

    print("El mensaje encriptado es: ",encriptado)


#DESENCRIPTAR EL MENSAJE
if op==2:
    msg=input("Escribe el mensaje encriptado: ").upper()
    llave=int(input("Dame la llave en la que deseas encriptar: "))
    for i in range (0,len(msg)):
        posicion=ABC.find(msg[i])
        if posicion>=0:
            indice=posicion-llave
            if indice>=26:
                indice=indice-26
            desencriptado+=ABC[indice]    
        else:
            desencriptado+=" "
             

    print("El mensaje desencriptado es: ",desencriptado)





    