#lista entrada ordenada
st = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '.']
#print(st)
#print(len(st))

#reflector (lo que se vizualizara)
rf = ['A', 'X', 'B', 'C', 'D', 'E', 'F', 'G', 'D', 'I', 'J', 'K', 'G', 'M', 'K', 'M', 'I', 'E', 'B', 'X', 'F', 'T', 'C', 'V', 'V', 'J', 'A', 'T']
#print(rf)
#print(len(rf))

#TODAS LAS LISTAS DEBEN DE IR EN ORDEN ALEATORIO ORDENDAS (se toma en cuenta . y espacio)
#lista derecha desordenada
r_der = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', ' ', 'N', '.', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
#print(len(r_der))

#lista media desordenada
r_med = ['.', 'A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', ' ', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
#print(len(r_med))

#lista izquierda desordenada
r_izq = ['E', 'K', 'M', 'F', 'L', 'G', ' ', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', '.', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
#print(len(r_izq))

#hacer listas de listas 
rotor_izq = []
rotor_med = []
rotor_der = []

#unir las listas entre si
for i in zip(st, r_izq): #izquierdo
    rotor_izq.append([i[0], i[1]])
    
for i in zip(st, r_med): #medio
    rotor_med.append([i[0], i[1]])
    
for i in zip(st, r_der): #derecho
    rotor_der.append([i[0], i[1]])

#print(rotor_der)

'''
#comprobar contruccion de las listas (rotores)
print(f'Reflector Rot_Izq Rot_Med Rot_Der Teclado')

for elem in zip(rf, rotor_izq, rotor_med, rotor_der, st):
    print(f'{elem[0]}    {elem[1][0]} - {elem[1][1]}    {elem[2][0]} - {elem[2][1]}    {elem[3][0]} - {elem[3][1]}    {elem[4]}')
'''

#mover de lugar (primero-ultimo) para el giro
def avanzar_rotor(rotor, paso):
    cuenta = 0
    while cuenta < paso:
        rotor.append(rotor.pop(0))
        cuenta += 1
    return rotor

#posicionar de acuerdo a la posicion inicial
def conf_rotores(clave_inicial):
    while clave_inicial.upper()[0] != rotor_izq[0][0]:
        rotor_izq.append(rotor_izq.pop(0))
        
    while clave_inicial.upper()[1] != rotor_med[0][0]:
        rotor_med.append(rotor_med.pop(0))

    while clave_inicial.upper()[2] != rotor_der[0][0]:
        rotor_der.append(rotor_der.pop(0))

conf_rotores('HIT')    #CONFIGURAR LOS ROTORES A TU MANERA

'''
#comprobar contruccion de las listas (rotores)
print(f'Reflector Rot_Izq Rot_Med Rot_Der Teclado')

for elem in zip(rf, rotor_izq, rotor_med, rotor_der, st):
    print(f'{elem[0]}    {elem[1][0]} - {elem[1][1]}    {elem[2][0]} - {elem[2][1]}    {elem[3][0]} - {elem[3][1]}    {elem[4]}')
'''

#funcion de ida 
def señal_ida(rotor, indice, verbose=False):
    
    letra_entrada = rotor[indice][1]
    indice_salida = 0
    for pares in rotor:
        if pares[0] != letra_entrada:
            indice_salida += 1
        else:
            break
    return letra_entrada, indice_salida

#print(señal_ida(rotor_der, 2))

#funcion de vuelta
def señal_vuelta(rotor, indice, verbose=False):
    
    letra_entrada = rotor[indice][0]
    indice_salida = 0
    for pares in rotor:
        if pares[1] != letra_entrada:
            indice_salida += 1
        else:
            break
    return letra_entrada, indice_salida

#print(señal_vuelta(rotor_izq, 10))

#buscar su letra par en el reflector
def indice_reflector(disco, indice, verbose=False):
    letra_entrada = disco[indice]
    if indice == (len(disco) - 1):
        for i in range(len(disco)):
            if disco[i] == letra_entrada:
                return letra_entrada, i
    else:
        for j in range(indice + 1, len(disco)):
            if disco[j] == letra_entrada:
                return letra_entrada, j
            else:
                for k in range(indice):
                    if disco[k] == letra_entrada:
                        return letra_entrada, k

'''
#comprobar los pares
for i in range(len(rf)):
    print(indice_reflector(rf, i))                    
'''

def enigma(mensaje, clave):
    
    conf_rotores(clave)
    
    mensaje_final = []
    for i in mensaje.upper():
        avanzar_rotor(rotor_der, 1)
        if rotor_der[-1][0] == 'V':
            avanzar_rotor(rotor_med, 1)
            if rotor_med[-1][0] == 'Q':
                avanzar_rotor(rotor_izq, 1)
                
        indice_entrada = st.index(i)
        
        primer_paso = señal_ida(rotor_der, indice_entrada)
        segundo_paso = señal_ida(rotor_med, primer_paso[1])
        tercer_paso = señal_ida(rotor_izq, segundo_paso[1])
        rebote = indice_reflector(rf, tercer_paso[1])
        cuarto_paso = señal_vuelta(rotor_izq, rebote[1])
        quinto_paso = señal_vuelta(rotor_med, cuarto_paso[1])
        sexto_paso = señal_vuelta(rotor_der, quinto_paso[1])
        mensaje_final.append(st[sexto_paso[1]])
        
    mensaje_str = ''.join(mensaje_final)
    return mensaje_str

print(enigma("IVBKQWYDIFGRPRZ","XHU"))



