
ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ "
ABCI="ZYXWVUTSRQPONMLKJIHGFEDCBD "
encriptado=[]

print("ATBASH")
op=int(input("De las siguientes opciones \n1)Encriptar \n2)Desencriptar \n¿Que es lo que quieres hacer: "))

#ENCRIPTAR
if op==1:
    msg=input("Escribe el mensaje que quieres encriptar= ").upper()
    for i in range(0,len(msg)):
        pos=ABC.find(msg[i])
        encriptado.append(ABCI[pos])

    print("El mensaje encriptado en ATBASH es->",encriptado)

#DESENCRIPTAR
if op==2:
    msg=input("Escribe el mensaje que quieres encriptar= ").upper()
    for i in range(0,len(msg)):
        pos=ABCI.find(msg[i])
        encriptado.append(ABC[pos])

    print("El mensaje encriptado en ATBASH es->",encriptado)


'''salida=""
msg=input("introduce el texto: ")

    for letra in msg.upper():
        if letra in ABC:
            indice=ABC.index(letra)
        salida += ABCI[indice]
    print(salida)

    salida2=""
    for letra in msg.upper():
        if letra in ABC:
            indice=ABC.index(letra)
        salida2 += ABC[(len(ABC)-1)-indice]
    print(salida2)
    '''


