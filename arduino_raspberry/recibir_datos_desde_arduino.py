import serial
import RPi.GPIO as GPIO
import time
from numpy import*
GPIO.setwarnings(False)

led = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

arduino= serial.Serial('/dev/ttyUSB1',baudrate=9600, timeout=3.0)#nombre de la tarjeta serial que esta el arduino
arduino.flushInput()#limbia lo que hay dentro del buffer antes de leer el dato


def get_distancia (line):
    if int(line) < 20:
        dato = "1"
    else :
        dato="0"
    return dato
#arduino.open()
while True:
    try:#try y except es para que no se genere error al romper el codigo cuando esta corriendo 
        
        lineBytes = arduino.readline()#lee los datos que vienen a traves del puerto serial
        line = lineBytes.decode('latin-1').strip()#decodifica a traves de latin-1 (formato unicode que eprmite convertir los bytes desde el arduino a string o valor, el strip elimina cualquier caracter extra dentro
        #print(line,"cm") #EL VALOR HAY Q HABLARLO DE FORMA DE UMBRAL, SI ESTA DEBAJO DE ESE VALOR O NO, DEBE HACER ALGO 
        #time.sleep(0.5)
        arreglo =array(line)
        print(array)
#         arreglo=[  ]
#         sharp=line[0:2]
#         print(len(line))
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(led, GPIO.OUT)
        if int(line) < 25:
            GPIO.output(led, True)
        if int(line) > 28:
            GPIO.output(led, False)
            
        get_distancia(line)
        mensaje = get_distancia(line).encode('latin-1') #codifica el mensaje en latin -1 para que llegue al arduino
        arduino.write(mensaje)# envia el mensaje por serial cada 500ms
#         time.sleep(0.5)
        
       
    
    except KeyboardInterrupt:
        break
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
GPIO.cleanup()
arduino.close()