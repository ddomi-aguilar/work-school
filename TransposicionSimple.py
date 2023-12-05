import math
msg=input('INTRODUCE EL MENSAJE ->> ').upper().replace(" ","")
key=int(input('INTRODUCE LA LLAVE DE TU MENSAJE ->> '))
msgX=list(msg)
op=int(input("¿QUE ES LO QUE DESEAS HACER? \n 1)ENCRIPTAR \n 2)DESENCRIPTAR \n INTRODUCE EL NUMERO->> "))

if op==1:

    #determinar las filas y columnas del arreglo
    print('TU MENSAJE A ENCRIPTAR ES->> ',msg,'CON LA LLAVE->>',key)
    columnas=key
    filas= int(math.ceil(float(len(msgX)) / float(key)) )

    #Definicion de la matriz CONSTRUCCION
    matriz=[]
    pos=0

    for i in range(filas):
        matriz.append([])
        for j in range (columnas):
            matriz[i].append(msgX[pos] if pos < len (msgX)else None)
            pos +=1
    #print(msgX)
    #print(matriz)

    #Orden de la matriz como sera ENCRIPTADA
    recorrer=0
    a=0
    texto=''
    while recorrer != key:
        columna=[fila[a] for fila in matriz]
        recorrer=recorrer+1
        a=a+1
        texto=texto+"".join([str(_)for _ in columna]).replace("None","")
    
    #print(texto) #impresion del texto encriptado

    #dividir la frase cada 5 caracteres
    sep = [texto[i:i+5] for i in range(0,len(texto), 5)]
    print("\n TU MENSAJE ENCRIPTADO ES->>",sep)
    print(texto)

if op==2:
    print('TU MENSAJE A DESENCRIPTAR ES->> ',msg,'CON LA LLAVE->> ',key)
    filas=key 
    columnas= int(math.ceil(float(len(msg)) / float(key)) )
    espacios=(columnas*filas)-len(msg) #espacios que se deben de tener en cuenta

    #Definicion de la matriz CONSTRUCCION
    matriz=[""]*columnas
    col=0
    fil=0


    for i in msg:
        matriz[col] += i
        col += 1

        if (col == columnas) or (col == columnas - 1) and (fil >= filas - espacios):
            col = 0
            fil += 1
    print("".join(matriz)) #.join SIRVE PARA JUNTAR LO QUE ESTA DENTRO DE UN ARREGLO

