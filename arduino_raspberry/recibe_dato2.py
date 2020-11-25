import serial
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.cleanup()
led = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)


arduino= serial.Serial('/dev/ttyUSB0',baudrate=9600)
#arduino.flushInput()

def get_distancia (cadena):
    if int(cadena) < 20:
        dato = "1"
    else :
        dato="0"
    return dato

while True:
    
    
    cadena = arduino.readline()
    
#     for sharp, ultra in cadena.decode() !='':
#         print(sharp.decode())

    
    #print(s.code())
  
#     if (cadena.decode() !=''):
    #print(cadena.decode())
    
    #time.sleep(1)
#     
    get_distancia(cadena)
    mensaje = get_distancia(cadena).encode() #codifica el mensaje en latin -1 para que llegue al arduino
    arduino.write(mensaje)# envia el mensaje por serial cada 500ms
#     #time.sleep(0.5)
    
    
    GPIO.cleanup()

#     x=input("Introduzca un comando: ")
#     
#     arduino.write(x.encode())
    


