import serial
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

led = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

ser= serial.Serial('/dev/ttyUSB0', 9600)#nombre de la tarjeta serial que esta el arduino
ser.flushInput()#limbia lo que hay dentro del buffer antes de leer el dato

def get_distancia (line):
    if int(line) < 20:
        dato = "1"
    else :
        dato="0"
    return dato

while True:
    try:#try y except es para que no se genere error al romper el codigo cuando esta corriendo 
        
        lineBytes = ser.readline()#lee los datos que vienen a traves del puerto serial
        line = lineBytes.decode('latin-1').strip()#decodifica a traves de latin-1 (formato unicode que eprmite convertir los bytes desde el arduino a string o valor, el strip elimina cualquier caracter extra dentro
        #print(line,"cm") #EL VALOR HAY Q HABLARLO DE FORMA DE UMBRAL, SI ESTA DEBAJO DE ESE VALOR O NO, DEBE HACER ALGO 
        #int(line)
        
        if int(line) < 20:
            GPIO.output(led, True)
        if int(line) > 20:
            GPIO.output(led, False)
            
        get_distancia(line)
        mensaje = get_distancia(line).encode('latin-1') #codifica el mensaje en latin -1 para que llegue al arduino
        ser.write(mensaje)# envia el mensaje por serial cada 500ms
        time.sleep(0.5)
        
    
    except KeyboardInterrupt:
        break
        
        