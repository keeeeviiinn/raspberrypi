from picamera import PiCamera
from time import sleep

camara = PiCamera()
camara.start_preview()
sleep(5)
camara.capture('/home/pi/Pictures/captura.jpg') #se coloca la direccion en la q se guarda
                                             #y al final el nombre y extension de la foto
camara.stop_preview()