import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

trig=24
echo=23
led=25

GPIO.setmode(GPIO.BCM)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(led, GPIO.OUT)


# try:
#     while True:
def sensor_ultrasonico():        
    GPIO.output(trig, GPIO.LOW)
    time.sleep(0.0001)
        
    GPIO.output(trig, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig, GPIO.LOW)
        
    while True:
        pulso_inicio = time.time()
        if GPIO.input(echo) == GPIO.HIGH:
            break
        
    while True:
        pulso_fin = time.time()
        if GPIO.input(echo) == GPIO.LOW:
            break
        
    duracion = pulso_fin - pulso_inicio
        
    distancia = (34300*duracion)/2
        
    print("Distancia: %.2f cm" %distancia)
    
    if distancia < 20:
        GPIO.output(led, GPIO.HIGH)
    if distancia > 23:
        GPIO.output(led, GPIO.LOW)

        
#         if distancia < 20:
#             GPIO.output(led, GPIO.HIGH)
#         if distancia > 23:
#             GPIO.output(led, GPIO.LOW)
            
try:
    while True:
        sensor_ultrasonico()
        
        
        
        
finally:        
    GPIO.cleanup()