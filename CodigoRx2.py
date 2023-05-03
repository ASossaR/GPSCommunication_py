import serial 
import time
import statistics as stat

ser = serial.Serial('/dev/ttyAMA0',19200)
header = 'PT_'
stop = "xF0F"
fin = "finfinfinfinfinfinf"
finish = 'stopstopstopstopsto'
buffer = ''
msj = ''
no_enviar = True 
recibido = 0
mensaje = ''
mensaje_pas = ''
true_recive = "Recepcion exitosa"
iterador = 1

f = open('DatosGPS.txt', 'w')

def Save_messaje(): #guardara en un archivo 
        global iterador
        if mensaje_pas[0] == '+':
                f.write(str(header) + str(iterador) + ' ')
                f.write(str(mensaje_pas))
                iterador += 1
        if mensaje_pas[0] == '-':
                f.write('  ')
                f.write(str(mensaje_pas))
                f.write('\n')
                
while mensaje != fin:
        recibido = 0
        while recibido < 40: #comprobación, falta hacer tiempo de espera o cantidad de preguntas
                buffer = ser.read_until(b'xF0F').decode('ascii')
                #print(buffer)
                if buffer[0:3] == 'PT_' and buffer[len(buffer) - 4:len(buffer)] == stop: #Parametros aceptados
                        #print ("formato aceptado")
                        mensaje = buffer[len(buffer)-23:len(buffer)-4]
                        #print("mensaje: ", mensaje)
                        if mensaje_pas == mensaje:
                                recibido += 1 
                        if recibido > 1:
                                if mensaje_pas != mensaje:
                                        print("Mensaje guargado exitosamente:", mensaje_pas, "\n\n")
                                        Save_messaje()
                                        recibido = 41 	
                                else:
                                        print("notificación de cierre enviada")
                                        ser.write(true_recive.encode('utf-8'))
                        mensaje_pas = mensaje
        if mensaje == finish:
                ser.write(true_recive.encode('utf-8'))
                break
        #ir a escribir mensaje
        #Guargar
f.closed