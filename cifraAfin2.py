#Se puede realizar directamente con las librerias incluidas en python
from sympy.crypto.crypto import encipher_affine, decipher_affine
import random,crip

ABC = "ABCDEFGHIJKLNMÑOPQRSTUVWXYZ¿?!¡#$%&/()='\+*~-_{|}°¬[:],;^<>1234567890@abcdefghijklmnñopqrstuvwxyz"
op= int(input("¿QUE QUIERES HACER? \n 1)CIFRAR \n 2)DESCIFRAR \nINTRODUCE TU RESPUESTA -> "))
    
if op==1:
    msg=input("INTRODUCE TU MENSAJE A ENCRIPTAR -> ")
    a=int(input("INTRODUCE EL VALOR DE A -> "))
    b=int(input("INTRODUCE EL VALOR DE B -> "))
    encriptado=encipher_affine(msg,(a,b))
    print(encriptado)    

elif op==2:
    msg=input("INTRODUCE TU MENSAJE A DESENCRIPTAR -> ")
    a=int(input("INTRODUCE EL VALOR DE A -> "))
    b=int(input("INTRODUCE EL VALOR DE B -> "))
    desencriptado=decipher_affine(msg,(a,b))
    print(desencriptado)
            

      