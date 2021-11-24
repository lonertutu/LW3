from picamera import PiCamera
from time import sleep

camera = PiCamera()

def take_photo(name):
    camera.start_preview()
    time.sleep(5)
    camera.capture("\\light\data\\" + name + ".jpeg")
    camera.stop_preview()