from tkinter import *
from PIL import Image, ImageTk
import RPi.GPIO as GPIO
import time
import numpy as py
from threading import Thread
from queue import Queue
import csv
import sys
import random
import board
import busio
import adafruit_vl53l0x



pin_motorA=18
pin_motorB=33

GPIO.setup(pin_motorA, GPIO.OUT)  #So we need to connect motor A to GPIO.18. also named pin 12 when we use
pwm=GPIO.PWM(pin_motorA,50)

#GET VALUE OF t1 and t2 from zemax_distance.csv file
M="2"
t1=0
t2=0
csv_file=csv.reader(open('zemax_distance.csv', "r"), delimiter=",")
for row in csv_file:
    if M==row[0]:
        print(row)
        distance_M=row
        t1=distance_M[1]            #t1 is the distance between LA 1257-A and LD 2568-A
        t2=distance_M[2]            #t1 is the distance between LD 2568-A and LA 1289-A
M=float(M)
t1=float(t1)
t2=float(t2)
print("DISTANCE WE ARE AIMING FOR", t1)
Top=t1+(t1*10/100)
print ("Top value acceptable",Top) #We accept a 10% error. This is high. Ideally, when a better distance sensor will be found, we should  have a lower tolerance
Bottom=t1-(t1*10/100)
print ("Bottom value acceptable", Bottom)
# print(t2)

i2c=busio.I2C(board.SCL, board.SDA) #connect to distance sensor A
vl53 = adafruit_vl53l0x.VL53L0X(i2c)
pwm.start(0)


while True:
    d1_=0
    count=0
    average=10
    for count in range(average):
        d1=vl53.range
        d1_=d1_+d1
        count+=1
    Distance=(d1/count)*10  #We take 10 measurements of the value obtained from the distance sensor and we average
    print("Actual Distance", Distance)

    if Distance>Bottom and Distance<Top: #If the distance obtained by the sensor is acceptable, we are done!

       print ("ok")
        break
    time.sleep(2)
    if Distance>Top:
        #If the distance is further away than what is acceptable, we make the motor move it closer
        print("too far")
        pwm.ChangeDutyCycle(9)
        #Various values were tested with the ChangeDutyCycle
        #to understand which value makes the lense gets closer to other one and which one makes it
        # go further
        time.sleep(1)

    time.sleep(2)
    if Distance<Bottom:
        #If the distance is closer than what is acceptable, we make the motor move it further
        print("too close")
        pwm.ChangeDutyCycle(2)
        time.sleep(1)
    time.sleep(2)


pwm.stop()

GPIO.cleanup() # GPIO.cleanup() at the end of the code commanding the Raspberry Pi is important (clean the ports before the next use)
