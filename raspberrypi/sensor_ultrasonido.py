import RPi.GPIO as GPIO
import time

#configuracion de los pines

GPIO.setmode(GPIO.BOARD)

TRIGER = 14
ECHO = 15
led = 18

#configuracion de las salidas

GPIO.setup(TRIGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

print("Medución ultrasonico")

try:
	while True:
		GPIO.output(TRIGER, False)
		time.sleep(0.5)
		
		GPIO.output(TRIGER, True)
		time.sleep(0.00001)
		GPIO.output(TRIGER, False)
		inicio = time.time()
		
		while GPIO.input(ECHO) ==0:
			inicio=time.time()
			
		while GPIO.input(ECHO) ==1:
			final = time.time()
			
		t = final-inicio
		distancia_tiempo = t*34000
		distancia= distancia_tiempo/2
		
		print("Distancia = %.1fcm"%distancia)
		
# except(KeyboardInterrupt):
# 	GPIO.cleanup()
