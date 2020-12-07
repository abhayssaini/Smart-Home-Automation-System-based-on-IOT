import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN) #PIR
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4
relay_pin = 23
GPIO.setup(relay_pin,GPIO.OUT)
 


try:
    
    while True:
        if GPIO.input(18):
           print("Motion Detected...")
           
           humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
            
           if humidity is not None and temperature is not None:
                print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
                GPIO.output (relay_pin,GPIO.LOW)
                if temperature > 30.0:
                   GPIO.output (relay_pin,GPIO.HIGH)
                else:
                    
                   GPIO.output (relay_pin,GPIO.LOW) 
                    
                time.sleep(2) #to avoid multiple detection
            
            
                    
        else:
            print("motion not Detected...")
            GPIO.output (relay_pin, GPIO.HIGH)      
            
            time.sleep(1) #loop delay, should be less than detection delay
            
        
except:
    GPIO.cleanup()

