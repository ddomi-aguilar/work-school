msg=str(input("ENCRIPTACION POR PARES \n ESCRIBA EL MENSAJE QUE QUIERE ENCRIPTAR ->> ").upper())
print("\nTU MENSAJE ENCRIPTADO ES")

for i in range(len(msg)): #PARES
    if i % 2 != 0:
        print(msg[i],end='')
    
for j in range(len(msg)): #IMPARES
    if j % 2 == 0:
        print(msg[j],end='')
    

    