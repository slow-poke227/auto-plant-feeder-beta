#!/usr/bin/python3
import time
import RPi.GPIO as GPIO
import Adafruit_DHT
import datetime

#number of water moisture sensor pin
input_pin = 23



def boardSetup():
        GPIO.setup(GPIO.BOARD)
        GPIO.setup(input_pin, GPIO.IN)

def boardCleanup():
        GPIO.cleanup()


def getStatus():
        global input_pin
        return GPIO.input(input_pin)

def checkEnv():
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        writeToFile(humidity, temperature)
        print(humidity)
        print(temperature)

def getStatus():
        return GPIO.input(input_pin)

def writeToFile(x, y):
        foo = open("*file",  "w")
        foo.write(x)
        foo.write(",")
        foo.write(y)
        foo.write(",")
        foo.close()

def getLastWatered():
        foo = open("*file", "r")
        foo.readline()
        foo.close()

def checkTime():
        #initialization for timeCheck
        now = datetime.datetime.now()
        today7am = now.replace(hour=7, minute=0, second=0, microsecond=0)
        today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
        today5pm = now.replace(hour=17, minute=0, second=0, microsecond=0)
        today6pm = now.replace(hour=18, minute=0, second=0, microsecond=0)
        # if time is between an interval (a = morning, b = afternoon)
        if today7am < now < today8am or today5pm < now < today6pm:
                # if plants not watered
                wet = getStatus()
                if wet == False:
                        waterPlants()

def waterPlants():
        #gpioXX = ON
        time.sleep(10)
        #gpioXX = OFF

if __name__ == "__main__":
        try:
                boardSetup()
                checkEnv()
                # checkTime calls waterPlants() if necessary
                # checkTIme will also call camCheck()
                checkTime()
                boardCleanup()
        except KeyboardInterrupt:
                GPIO.cleanup()
