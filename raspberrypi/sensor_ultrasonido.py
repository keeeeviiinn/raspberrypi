import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
#configuracion de los pines

GPIO.setmode(GPIO.BCM)

TRIGER = 23
ECHO = 24
led = 25

#configuracion de las salidas

GPIO.setup(TRIGER, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

print("Medución ultrasonico")

r=True
while True:
	GPIO.output(TRIGER, False)
	time.sleep(0.001)
		
	GPIO.output(TRIGER, True)
	time.sleep(0.00001)
	GPIO.output(TRIGER, False)
	inicio = time.time()
		
	while GPIO.input(ECHO) ==0:
		inicio=time.time()
		
			
	while GPIO.input(ECHO) ==1:
		final = time.time()
		
			
	t = final-inicio
	distancia_tiempo = t/0.000058
	distancia= distancia_tiempo/2
	print(distancia)	
		#print("Distancia = %.1fcm"%distancia_tiempo)
	    #print(distancia_tiempo)
		
# 	if distancia <20:
#         GPIO.output(led, True)
#             
#     if distancia > 20:
#         GPIO.output(led, False)
	    
#except(KeyboardInterrupt):
 #   GPIO.cleanup()
