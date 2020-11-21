#Configuración de pines, ejemplo de encender y apagar un led

import RPi.GPIO as GPIO # IMPORTA LA LIBRERIA DE LOS PINES (ENUMERADO EN FORMA 		                           FISICA PIN 5 (BOARD)

from time import sleep # libreria para hacer los delay
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # CON BOARD SE SELECCIONA EL NUMERO DEL PIN FISICO EN LA TARJETA 
GPIO.setup(25, GPIO.OUT) # PIN 7 COMO SALIDA

R= True
while R==True:
     GPIO.output(25,True) # ENVIA UN PULSO EN ALTO AL PIN 7
     
     sleep(1)       # pausa de 1s
     GPIO.output(25,False) # COLOCA EN BAJA EL PIN
     
     sleep(1)