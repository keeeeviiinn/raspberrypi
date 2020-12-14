from picamera import PiCamera
from time import sleep

#si se ve a traves del monitor por HDMI, se observa la imagen al momento 
 
camara = PiCamera()
camara.start_preview()
sleep(20)
camara.stop_preview()
