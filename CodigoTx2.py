import serial 
import time
import statistics as static 

archivo = '/home/sossa/Documentos/Taller de Comu/DatosGPS.txt'
ser = serial.Serial('/dev/ttyUSB0', 19200)
print(ser.name)
header = 'PT_'
stop = "xF0F"
finish = 'PT_201stopstopstopstopstoxF0F'
true_recive = "Recepcion exitosa"
ser.timeout = 0.1
palabras = []
moco   = 'PT_mocomocomocomocomocxF0F'
y = ''

#abrir un archivo
with open(archivo,"r") as archivo:
	for lineas in archivo:
		#print('lineaa: ', lineas)
		palabras.extend(lineas.split())
		#print (palabras)



#metodo
for i in range(len(palabras)):
	if i%3 == 0:
		latitud = palabras[i] + palabras[i+1]  + stop
		longitud = palabras[i] + palabras[i+2] + stop
		print('Linea: ', i)
		print('Latitud:  ', latitud)
		print('Longitud: ', longitud)
		print('\n')
		
		confirmacionRx = True 
		while confirmacionRx: #Para Latitud
			#print(latitud)
			ser.write(latitud.encode('utf-8'))
			x = ser.read_until(b'xF0F').decode("ascii")
		
			if(x == true_recive):
				confirmacionRx = False
				print('Rx recibe')
			else:
				confirmacionRx = True 
				print('Sigo enviando latitud')

		#ser.write(moco.encode('utf-8'))

		#print(moco)
		x = moco
		confirmacionRx = True 
		while confirmacionRx: #Para Longitud
			#print(longitud)
			ser.write(longitud.encode('utf-8'))
			x = ser.read_until(b'xF0F').decode("ascii")
		
			if(x == true_recive):
				confirmacionRx = False
				print('Rx recibe')
			else:
				confirmacionRx = True 
				print('Sigo enviando longitud')


while y  != true_recive:
	y = ser.read_until(b'xF0F').decode("ascii")
	if(y == true_recive):
		break
	print('Terminar')
	ser.write(finish.encode('utf-8'))