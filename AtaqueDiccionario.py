import math
LETRAS_MAYUSCULAS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LETRAS = LETRAS_MAYUSCULAS + LETRAS_MAYUSCULAS.lower()+"\t\n "

def leer_diccionario():
    archivo = open('diccionario_espanol.txt',encoding = "utf8")
    palabras_espanol = {}
    for palabra in archivo.read().split('\n'):
        palabras_espanol[palabra] = None
    archivo.close()
    return palabras_espanol


PALABRAS_ESPANOL = leer_diccionario()

def limpiar_texto(mensaje):
    letras =[]

    for simbolo in mensaje:
        if simbolo in LETRAS: 
            letras.append(simbolo)
    return ''.join(letras)


def es_espanol(mensaje):
# Por defecto, se considera que el mensaje tiene sentido
# en castellano si Rlex >= 0,50
    mensaje = limpiar_texto(mensaje).upper()
    longitud = len(mensaje)
    texto = ''
    for palabra in PALABRAS_ESPANOL:
        if mensaje.find(palabra) != 1:
            texto += palabra
    coef = len(texto)/longitud
    parte_decimal,parte_entera = math.modf(coef)
    if parte_decimal >= 0.50:
        return True,coef ,"ESPAÑOL"
        
    else:
        return False,coef,"INGLES"
        

 
