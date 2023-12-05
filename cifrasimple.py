import random
abc= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def generar_clave():
    llave=list(abc)
    random.shuffle(llave)
    return "".join(llave)

def encriptar(mensaje,clave):
    encriptado=''
    for letra in mensaje:
        pos=abc.find(letra)
        if abc.find(letra)!=-1:
            encriptado+=clave[pos]
        else:
            encriptado+=letra
    return encriptado

def desencriptar(mensaje,clave):
    desencriptado=''
    for letra in mensaje:
        pos=clave.find(letra)
        if clave.find(letra)!=-1:
            desencriptado+=abc[pos]
        else:
            desencriptado+=letra
    return desencriptado


msg=input("ESCRIBA SU MENSAJE A CIFRAR -> ").upper()
llave=generar_clave()
a=encriptar(msg,llave)
print(a)
print(llave)

b=desencriptar(a,llave)
print(b)
    