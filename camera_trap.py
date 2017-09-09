import RPi.GPIO as GPIO
import time
import picamera

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
#GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
       i=GPIO.input(11)
       if i==0:                 #When output from motion sensor is LOW
             print "No intruders",i
             #GPIO.output(3, 0)  #Turn OFF LED
             time.sleep(0.5)
       elif i==1:               #When output from motion sensor is HIGH
             print "Intruder detected",i
             with picamera.PiCamera() as camera:
                 camera.rotation = 180
                 camera.start_preview()
                 time.sleep(2)
                 camera.capture('/home/pi/projects/camera_trap/pictures/latest.jpg')
                 camera.capture('/home/pi/projects/camera_trap/pictures/capture_{}.jpg'.format(int(time.time())))
                 camera.stop_preview()

             #GPIO.output(3, 1)  #Turn ON LED
             time.sleep(10)
