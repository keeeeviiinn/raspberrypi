import os #importa sistema operativo
import datetime as dt #importar fecha
from picamera import PiCamera
from time import sleep
from signal import pause

destino = '/home/pi/Videos'  # ruta de destino en que se guarda
camara = PiCamera()

def grabar_video():
	nombrevideo = os.path.join(destino,dt.datetime.now().strftime('%Y-%m-%d_%H.%M.                      %S.h264')) #coloca como nombre Y de año,mes dia(d), hora(H), minuto
	camara.start_preview()
	camara.start_recording(nombrevideo)

def alto_video():
	camara.stop_recording()
	camara.stop_preview()

grabar_video()
sleep(10)
alto_video()