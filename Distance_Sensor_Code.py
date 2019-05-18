from gpiozero import LED
import RPi.GPIO as GPIO
import time
import signal
import sys

#Setup to use Pi pin numbers
GPIO.setmode(GPIO.BCM)

#Setup for GPIO pins
pinTrigger = 18
pinEcho = 24

#LED Setup
led = LED(23)

def close(signal, frame):
    print("turning off ultrasonic distance detection")
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, close)


#Setup for GPIO input and output channels
GPIO.setup(pinTrigger, GPIO.OUT)
GPIO.setup(pinEcho, GPIO.IN)

while True:
    #set Trigger to HIGH
    GPIO.output(pinTrigger, True)
    #set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(pinTrigger, False)
    
    startTime = time.time()
    stopTime = time.time()
    
    #saving start time
    while 0 == GPIO.input(pinEcho):
            startTime = time.time()
            
    #saving time of arrival
    while 1 == GPIO.input(pinEcho):
            stopTime = time.time()
            
    #setup for time difference between start time and Time of arrival
    TimeElapsed = stopTime - startTime
    #multiply with the sonic speed (34300 cm/s)
    distance = (TimeElapsed * 34300) / 2
    
    print ("Distance: %.1f cm" % distance)
    
    #Setup for LED trigger to turn ON and OFF
    if distance <= 25:
        print("just the right distance")
        led.on()
        time.sleep(2)
        led.off()
    
    time.sleep(1)