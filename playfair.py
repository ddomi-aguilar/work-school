
key=input("ESCRIBE TU CLAVE -->").replace(" ","").upper()

#CONSTRUCCION DE LA MATRIZ
def matrizI(x,y,iniciar):
    return [[iniciar for i in range(x)] for j in range(y)]    
res=list()

#SUSTITUIR LAS LETRAS J -> I == TODAS POR I
for c in key: 
    if c not in res:
        if c=='J':
            res.append('I')
        else:
            res.append(c)

letra=0 
for i in range(65,91): 
    if chr(i) not in res:
        if i==73 and chr(74) not in res:
            res.append("I")
            letra=1
        elif letra==0 and i==73 or i==74:
            pass    
        else:
            res.append(chr(i))

#DEFINIR FORMA DE LA MATRIZ            
k=0
matriz=matrizI(5,5,0) 
for i in range(0,5): 
    for j in range(0,5):
        matriz[i][j]=res[k]
        k+=1

#print(matriz)   
    

#SABER EL LUGAR DE CADA LETRA
def locacion(c):
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(matriz):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
            

#ENCRIPTACION            
def encriptacion():  
    msg=str(input("MENSAJE QUE QUIERES ENCRIPTAR -->")).upper().replace(" ","")

    #AGREGAR/SUSTITUIR POR X CADA DOS (REPETIDAS-FALTA)            
    i=0
    for s in range(0,len(msg)+1, 2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]

    if len(msg)%2!=0:
        msg=msg[:]+'X'

    print("TEXTO CIFRADO: ",end=' ')

    #JUGAR CON LAS LOCACIONES DE LAS LETRAS, PARA TERMINAR DE CIFRAR 
    while i<len(msg):
        loc=list()
        loc=locacion(msg[i])
        loc1=list()
        loc1=locacion(msg[i+1])

        if loc[1]==loc1[1]:
            print("{}{}".format(matriz[(loc[0]+1)%5][loc[1]],matriz[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(matriz[loc[0]][(loc[1]+1)%5],matriz[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(matriz[loc[0]][loc1[1]],matriz[loc1[0]][loc[1]]),end=' ')    
        i=i+2 

    exit()       


#DESENCRIPTACION                 
def desencriptacion():  
    msg=str(input("MESAJE QUE QUIERES DESENCRIPTAR -->")).upper().replace(" ","")

    print("TEXTO DESIFRADO: ",end=' ')

    #JUGAR CON LAS LOCACIONES DE LAS LETRAS, PARA TERMINAR DE CIFRAR 
    i=0
    while i<len(msg):
        loc=list()
        loc=locacion(msg[i])
        loc1=list()
        loc1=locacion(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(matriz[(loc[0]-1)%5][loc[1]],matriz[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(matriz[loc[0]][(loc[1]-1)%5],matriz[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            print("{}{}".format(matriz[loc[0]][loc1[1]],matriz[loc1[0]][loc[1]]),end=' ')    
        i=i+2
    exit()                


#MENU
while(1):
    op=int(input("\n 1)ENCRIPTACION \n 2)DESENCRIPTACION \nESCRIBE TU ELECCION--> "))
    if op==1:
        encriptacion()
    elif op==2:
        desencriptacion()
    
   