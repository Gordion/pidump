import time
import picamera

with picamera.PiCamera() as camera:
    camera.rotation = 180
    camera.start_preview()
    time.sleep(2)
    camera.capture('/home/pi/projects/ant_watch/pictures/latest.jpg')
    camera.capture('/home/pi/projects/ant_watch/pictures/capture_{}.jpg'.format(int(time.time())))
    camera.stop_preview()
