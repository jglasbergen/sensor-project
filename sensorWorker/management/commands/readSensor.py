from channels import Group
from django.core.management import BaseCommand
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

def my_callback(channel):
    if GPIO.input(26):     # if port 25 == 1
        # print("Rising edge detected on 26")
        GPIO.output(18, GPIO.HIGH)
        Group("sensor").send({'text': "Button pushed"})
    else:                  # if port 256!= 1
        # print("Falling edge detected on 26")
        GPIO.output(18, GPIO.LOW)
        Group("sensor").send({'text': "Button released"})

class Command(BaseCommand):
    help = "Reading sensor on port 26"

    def handle(self, *args, **kwargs):
        GPIO.add_event_detect(26, GPIO.BOTH, callback=my_callback)

        while True:
            input("Press Enter when ready\n>")
            GPIO.cleanup()











    # help = "Simulates reading sensor and sending over Channel."

    # def handle(self, *args, **kwargs):
    #     x = 0
    #     while True:
    #         textToSend = "Sensor reading = " + str(x)
    #         Group("sensor").send({'text': textToSend})
    #         time.sleep(2)
    #         x = x + 1
    #         self.stdout.write("Sensor reading...." + str(x))
