import AtaqueDiccionario,math
msg="HLMNOOAUD"

desencriptado=" " 
#DESENCRIPTAR EL MENSAJE

for llave in range (1,len(msg)):
    filas=llave 
    columnas= int(math.ceil(float(len(msg)) / float(llave)) )
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
    



