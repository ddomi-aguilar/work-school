ABC = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890 ")

def main():
    msg=input("Escribe tu mensaje ->").upper().replace(" ","")
    llave="CINCO"
    op=int(input("Escribe el numero de lo que quieres hacer: \n1)ENCRIPTAR \n2)DESENCRIPTAR ->"))

    if op==1:
        cifrado=cifrar_mensaje(llave,msg)
    elif op==2:
        cifrado=descifrar_mensaje(llave,msg)
    print(cifrado)


def cifrar_mensaje(clave,mensaje):
    return cifrar(clave,mensaje,1)

def descifrar_mensaje(clave,mensaje):
    return cifrar(clave,mensaje,2)


def cifrar(clave,mensaje,op):
    cifrado=[]
    indice=0
    clave=clave.upper()

    for i in mensaje:
        num=ABC.find(i.upper())
        if num!=-1:
            if op==1:
                num+=ABC.find(clave[indice])
            elif op==2:
                num-=ABC.find(clave[indice])
            num%=len(ABC)
            if i.isupper():
                cifrado.append(ABC[num])
            elif i.islower():
                cifrado.append(ABC[num].lower())
            indice+=1
            if indice==len(clave):
                indice=0

        else:
            cifrado.append(i)
    return ('').join(cifrado)

if __name__ == '__main__':
    main()