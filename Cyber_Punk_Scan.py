import subprocess	#Importa los subprocess para la comunicación PING.
import socket		#Importa el socket para el Escaneo de puertos

print("	By:																				 ")
print("  ██████╗██╗   ██╗██████╗ ███████╗██████╗     ██████╗ ██╗   ██╗███╗   ██╗██╗  ██╗ ")
print(" ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║   ██║████╗  ██║██║ ██╔╝ ")
print(" ██║      ╚████╔╝ ██████╔╝█████╗  ██████╔╝    ██████╔╝██║   ██║██╔██╗ ██║█████╔╝  ")
print(" ██║       ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗    ██╔═══╝ ██║   ██║██║╚██╗██║██╔═██╗  ")
print(" ╚██████╗   ██║   ██████╔╝███████╗██║  ██║    ██║     ╚██████╔╝██║ ╚████║██║  ██╗ ")
print("  ╚═════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═╝      ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ")
print("																					 ")
		
host1 = input ("		IP O LINK A RECONOCER : ")	#Recibir la Dirección IP o el link.

#Función para hacer ping
def pingFull (host1):
	#Realiza solo 2 solicitudes de PING
	receptivo = subprocess.call(["ping", "-c", "2", host1])

	#Imprime que el host responde solicitudes PING
	if receptivo == 0:
		print("																		")
		print("		FELICIDADES ", host1, "ESTÁ RESPONDIENDO CORRECTAMENTE			")
		print("																		")
		print("		  SE ESTÁ REALIZANDO EL ESCANEO DE PUERTOS ABIERTOS				")
		print("																		")

	#SINO imprimirá lo siguiente	
	else:
		print("																		")
		print("					ERROR ", host1, "ES INALCANZABLE					")
		print("																		")

#Función verdadero de ciclo abierto
while True:
	#Función para que realice el pingfull
	pingFull(host1)
	#Si la IP o LINK funciona, hace un break y continua con la siguiente función del ESCANEO DE PUERTOS.
	if host1:
		break

puerto = int
#Corresponde a la importación de "SOCKET"
#Crea la Función "ESCANEAR" pra que el "HOST" que ingresamos, interactue con el puerto en un tiempo establecido.
def escanear(host2, puerto):
	try:
		#Llama a socket, para comunicarse a nivel de red.
		Socket = socket.socket()
		#Establece el tiempo de comunicación en 1 Segundo.
		Socket.settimeout(1)
		#Establece la comunicación del "HOST" que ingresamos y el puerto o rango a escanear.
		Socket.connect((host2, puerto))
		#Escriba una comunicación.
		Socket.send(b'Conectado')
		#Imprime los puertos ABIERTOS.
		print (" PUERTO = ",puerto," ABIERTO")

#Es la excepción para por puertos que estan cerrados
	except:
		(" PUERTO =",puerto,"CERRADO")

#Cierra la comunnicación
	finally:
		Socket.close()


#Función que llama a escanear en rangos de puertos.
host2 = host1

for puerto in range (1, 500):		
	#Utiliza la función ESCANEAR, concatenando la IP o LINK mas el puerto
	escanear(host2, puerto)

try:
	print ("														")
	print ("		EL ATAQUE DE RECONOCIMIENTO A FINALIZADO		")
	print ("														")

	guardar = open('REGISTRO_ESCANEO_CYBER_PUNK.txt', 'a')
		#ACA TENGO QUE LOGRAR GUARDAR LAS VARIABLES DE:
		#PUERTO CON SU RESPECTIVO SERVICIO ACTIVO.
	guardar.write ('LOG DE REGISTRO \n')
	guardar.close()

#	
#	guardar = open ('REGISTRO_ESCANEO.txt','w')
#	guardar.write("ERROR DE REGISTRO")

except:
	
	exit()
	print("ERROR DE REGISTRO")
	
	#Cuando ejecutas el programa que escribimos, el método open le dice a tu computadora que produzca un nuevo archivo de texto llamado holamundo.txt en la misma carpeta en la que creamos el programa archivo-salida.py. El parámetro w indica que pretendemos escribir contenido en este nuevo archivo utilizando Python.
