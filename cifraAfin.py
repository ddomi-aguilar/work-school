import sys,pyperclip,crip,random

ABC = "ABCDEFGHIJKLNMÑOPQRSTUVWXYZ¿?!¡#$%&/()='\+*~-_{|}°¬[:],;^<>1234567890@abcdefghijklmnñopqrstuvwxyz"
#print(len(ABC))

def main():

    op=int(input("¿QUE QUIERES HACER? \n 1)CIFRAR \n 2)DESCIFRAR \n 3)CREAR CLAVE \nINTRODUCE TU RESPUESTA -> "))

    if op == 1 :
        msg=input("ESCRIBE EL MENSAJE A ENCRIPTAR -> ")
        A=int(input("¿CUAL SERA EL VALOR DE A (0,97)-> "))
        B=int(input("¿CUAL SERA EL VALOR DE B (0,97)-> "))
        resultado=cifrar_msg(msg,A,B)

    elif op == 2 :
        msg=input("ESCRIBE EL MENSAJE ENCRIPTADO -> ")
        A=int(input("¿CUAL ES EL VALOR DE A (0,97)-> "))
        B=int(input("¿CUAL ES EL VALOR DE B (0,97)-> "))
        resultado=descifrar_msg(msg,A,B)
    elif op ==3:
        key=clave()
        print("TU CLAVE ES: ",key)           
        sys.exit()    
    else:
        print("NO ES VALIDO")

    print("Tu mensaje es -> ",resultado)
    pyperclip.copy(resultado)       

def clave ():
    while True:
        A= random.randint(0,len(ABC))
        B= random.randint(0,len(ABC))
        if crip.mcd(A,len(ABC)) == 1:
            return (A,B)
        
def revisar (A,B):
    if A not in range (0,97):
        print("NUMERO INVALIDO")
    if B  not in range (0,97):
        print("NUMERO INVALIDO")
    if crip.mcd(A,len(ABC)) != 1:
        print("NO SON COPRIMOS"%(A,len(ABC)))

def cifrar_msg (msg,A,B):
    revisar(A,B)
    cifrado=""
    for sim in msg :
        if sim in ABC:
            indice=ABC.find(sim)
            cifrado+=ABC[(indice * A + B)% len(ABC)]
        else:
            cifrado += sim 
    return cifrado

def descifrar_msg (msg,A,B):
    revisar(A,B)
    text=""
    inversoA=crip.invMod(A,len(ABC))

    for sim in msg:
        if sim in ABC:
            indice=ABC.find(sim)
            text+=ABC[(indice-B)*inversoA%len(ABC)]
        else:
            text += sim
    return text

if __name__ == '__main__':
    main()                    

           
