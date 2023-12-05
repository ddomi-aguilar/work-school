import sys

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
msg = str(input("¿Cual es tu mensaje a cifrar?--> "))
msg = msg.replace(' ', '').upper()
claveO = str(input("¿Cual es la clave?--> "))
claveO = claveO.replace(' ', '').upper()
clave = ''
cifrado = ''
descifrado = ''

if len(msg)>len(claveO):	
	for i in range(int(len(msg)/len(claveO))):		
		clave += claveO									
	clave += claveO[:len(msg)%len(claveO)]	

elif len(msg)<len(claveO):	
	clave = claveO[:len(msg)]	

elif len(msg)==len(claveO):	
	clave = claveO	

else:
	print ("ERROR")
	sys.exit(1) #indica un error y salir de programa


print ("MENSAJE -->" + msg)
print ("PALABRA CLAVE -->" + claveO)
print ()


#CIFRADO
for i in range(len(msg)):
	x = ABC.find(msg[i])	
	y = ABC.find(clave[i])
	suma = x+y	
	a = suma%len(ABC)	
	cifrado += ABC[a]	

print ("Mensaje cifrado--> " + cifrado)
print ()
	

#DESCIFRADO
for i in range(len(cifrado)):
	x = ABC.find(cifrado[i])	
	y = ABC.find(clave[i])	
	resta = x-y	
	a = resta%len(ABC)	
	descifrado += ABC[a]

print ("Mensaje descifrado--> " + descifrado)

sys.exit(0) #salida del programa normal